#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 02:20:09 2018

@author: jimhs
"""

# cook 6.12

import struct

from itertools import chain

polys = [
            [ (1.0, 2.5), (3.5, 4.0), (2.5, 1.5) ],
            [ (7.0, 1.2), (5.1, 3.0), (0.5, 7.5), (0.8, 9.0) ],
            [ (3.4, 6.3), (1.2, 0.5), (4.6, 9.2) ],
        ]

# generate bin file
def write_polys(filename, polys):
    # determin bound box
    flattened = list(chain(*polys))
    min_x = min(x for x, y in flattened)
    min_y = min(y for x, y in flattened)
    max_x = max(x for x, y in flattened)
    max_y = max(y for x, y in flattened)
    
    with open(filename, 'wb') as f:
        f.write(struct.pack('<iddddi',
                            0x1234,
                            min_x, min_y,
                            max_x, max_y,
                            len(polys)))
        
        for poly in polys:
            size = len(poly) * struct.calcsize('<dd')
            f.write(struct.pack('<i', size+4))
            for pt in poly:
                f.write(struct.pack('<dd', *pt))
                
class StructField:
    '''
    descriptor representing a simple structure field
    '''
    def __init__(self, format_, offset):
        self.format = format_
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            r = struct.unpack_from(self.format, instance._buffer, self.offset)
            return r[0] if len(r) == 1 else r

class NestedStruct:
    '''
    descriptor representing a nested structure
    '''
    def __init__(self, name, struct_type, offset):
        self.name = name
        self.struct_type = struct_type
        self.offset = offset
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            data = instance._buffer[self.offset:self.offset+self.struct_type.struct_size]
            result = self.struct_type[data]
            # save resulting structure back to avoid recomputation
            setattr(instance, self.name, result)
            return result
        
class StructureMeta(type):
    '''
    meta class that automatically creates StructureField descriptor
    '''
    def __init__(self, clsname, bases, clsdict):
        fields = getattr(self, '_fields_', [])
        byte_order = ''
        offset = 0
        for format_, fieldname in fields:
            if isinstance(format_, StructureMeta):
                setattr(self, fieldname, NestedStruct(fieldname, format_, offset))
                offset += format_.struct_size
            else:
                if format_.startswith(('@', '=', '<', '>', '!')):
                    byte_order = format_[0]
                    format_ = format_[1:]
                format_ = byte_order + format_
                setattr(self, fieldname, StructField(format_, offset))
                offset += struct.calcsize(format_)
        setattr(self, 'struct_size', offset)
        
class Structure(metaclass=StructureMeta):
    def __init__(self, bytedata):
#        self._buffer = memoryview(bytedata)
        self._buffer = bytedata
        
    @classmethod
    def from_file(cls, f):
        return cls(f.read(cls.struct_size))

class SizedRecord:
    def __init__(self, bytedata):
        self._buffer = memoryview(bytedata)
        
    @classmethod
    def from_file(cls, f, size_fmt, includes_size=True):
        sz_nbytes = struct.calcsize(size_fmt)
        sz_bytes = f.read(sz_nbytes)
        sz, = struct.unpack(size_fmt, sz_bytes)
        buf = f.read(sz - includes_size * sz_nbytes)
        return cls(buf)
    
    def iter_as(self, code):
        if isinstance(code, str):
            s = struct.Struct(code)
            for off in range(0, len(self._buffer), s.size):
                yield s.unpack_from(self._buffer, off)
        elif isinstance(code, StructureMeta):
            size = code.struct_size
            for off in range(0, len(self._buffer), size):
                data = self._buffer[off:off+size]
                yield code(data)
                
class Point(Structure):
    _fields_ = [
        ('<d', 'x'),
        ('d', 'y')
    ]

class PolyHeader(Structure):
    _fields_ = [
        ('<i', 'file_code'),
#            ('d', 'min_x'),
#            ('d', 'min_y'),
#            ('d', 'max_x'),
#            ('d', 'max_y'),
        (Point, 'min'), # nested struct
        (Point, 'max'), # nested struct
        ('i', 'num_polys')
    ]

def read_polys(filename):
    polys = []
    with open(filename, 'rb') as f:
        phead = PolyHeader.from_file(f)
        for n in range(phead.num_polys):
            rec = SizedRecord.from_file(f, '<i')
            poly = [ (p.x, p.y) for p in rec.iter_as(Point) ]
            polys.append(poly)
    return polys