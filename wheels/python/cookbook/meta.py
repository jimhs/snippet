#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 04:30:23 2018

@author: jimhs
"""

import weakref
import logging
import types
import abc
import operator
import sys

import collections
import bisect

from collections import OrderedDict
from inspect import Signature, Parameter, signature
from time import localtime

#from decorator import LazyProperty

# cookbook 9.13
class NoInstance(type):
    def __call__(self, *args, **kwargs):
        raise TypeError('cant instantiate directly')

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self.__instance = None
        super().__init__(*args, **kwargs)
        
    def __call__(self, *args, **kwargs):
        if self.__instance is None:
            self.__instance = super().__call__(*args, **kwargs)
            return self.__instance
        else:
            return self.__instance

class Cached(type):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()
    
    def __call__(self, *args):
        if args in self.__cache:
            return self.__cache[args]
        else:
            obj = super().__call__(*args)
            self.__cache[args] = obj
            return obj
        
class Spam(metaclass=Cached):
    def __init__(self, name):
        print('creating spam({!r})'.format(name))
        self.name = name
        
    @staticmethod
    def grok(x):
        print('spam.grok:',x)

# cookbook 8.13
# base class, use a descriptor to set value
class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class Typed(Descriptor):
    _expected_type = type(None)
    
    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError('expected '+ str(self._expected_type))
        super().__set__(instance, value)

# descriptors for enforcing value
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        if value < 0 :
            raise ValueError('expect >= 0')
        super().__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError("missing 'size' option")
        super().__init__(name, **opts)
    
    def __set__(self, instance, value):
        if len(value) > self.size :
            raise ValueError('size must be <= ' + str(self.size))
        super().__set__(instance, value)
        
# cookbook 9.14
# a set of descriptors for various types
#class Typed:
#    _expected_type = type(None)
#    def __init__(self, name=None):
#        self._name = name
#    
#    def __set__(self, instance, value):
#        if not isinstance(value, self._expected_type):
#            raise TypeError('expected '+ str(self._expected_type))
#        instance.__dict__[self._name] = value

#OPTIMIZE page 284~287 include some other similar methods    


class Interger(Typed):
    _expected_type = int

class Float(Typed):
    _expected_type = float

class String(Typed):
    _expected_type = str

class UnsignedInterger(Interger, Unsigned):
    pass

class UnsignedFloat(Float, Unsigned):
    pass

class SizedString(String, MaxSized):
    pass

# metaclass that use an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []
        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d['_order'] = order
        return type.__new__(cls, clsname, bases, d)
    
    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()
    
class Structure(metaclass=OrderedMeta):
    def as_csv(self):
        return ','.join(str(getattr(self, name)) for name in self._order)
    
_stock_formats = {
        'str_' : '{0.share} shares of {0.name} @{0.price}',
        'repr_' : 'Stock({0.name!r}, {0.share!r}, {0.price!r})',
        'desc_' : 'name={0.name!r}, share={0.share}, price={0.price}'
        
        }

class Stock(Structure):
#    name = String()
#    share = Interger()
#    price = Float()
    name = SizedString('name', size=4)
    share = UnsignedInterger('share')
    price = UnsignedFloat('price')
    
    #??? 'name' in __slots__ conflicts with class variable
    # __slots__ = ['name', 'share', 'price']
    
    def __init__(self, name, share, price):
        self.name = name
        self.share = share
        self.price = price
    
    # 8.1
    def __str__(self):
        return _stock_formats['str_'].format(self)
    
    #??? eval(repr(s)) == s, is False
    def __repr__(self):
        return _stock_formats['repr_'].format(self)
    
    def __format__(self, code):
        if code == '':
            code = 'desc_'
        fmt = _stock_formats[code]
        return fmt.format(self)
    
#    @decorator.lazyproperty
    @property
    def amo(self):
        print('calculating amo...')
        return self.share * self.price

# cookbook 9.14
# prevents duplicated method def       
class NoDupOrderedDict(OrderedDict):
    def __init__(self, clsname):
        self.clsname = clsname
        super().__init__()
    def __setitem__(self, name, value):
        if name in self:
            raise TypeError('{} already defined in {}'.format(name, self.clsname))
        super().__setitem__(name, value)
        
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d= dict(clsdict)
        d['_order'] = [name for name in clsdict if name[0] != '_']
        return type.__new__(cls, clsname, bases, d)
    
    @classmethod
    def __prepare__(cls, clsname, bases):
        return NoDupOrderedDict(clsname)

# duplicated example
class DupA(metaclass=OrderedMeta):
    def spam(self):
        pass
    def spam2(self):
        pass

# cookbook 9.16
# fixed parm signature
# make a signature for a func(x, y=42, *, z=None)
parms = [Parameter('x', Parameter.POSITIONAL_OR_KEYWORD),
         Parameter('y', Parameter.POSITIONAL_OR_KEYWORD, default=42),
         Parameter('z', Parameter.KEYWORD_ONLY, default=None)]

sig = Signature(parms)
# print(sig)

def func(*args, **kwargs):
    bound_value = sig.bind(*args, **kwargs)
    for name, value in bound_value.arguments.items():
        print(name, value)

# cookbook 9.16
# fixed parm signature 2
def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
             for name in names]
    return Signature(parms)

class SigStructure:
    __signature__ = make_sig()
    def __init__(self, *args, **kwargs):
        bound_value = self.__signature__.bind(*args, **kwargs)
        for name, value in bound_value.arguments.items():
            setattr(self, name, value)

# example
class SigStock(SigStructure):
    __signature__ = make_sig('name', 'share', 'price')

class SigPoint(SigStructure):
    __signature__ = make_sig('x', 'y')

# cookbook 9.17
class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('bad attribute name ' + name)
        return super().__new__(cls, clsname, bases, clsdict)

class NMCMRoot(metaclass=NoMixedCaseMeta):
    pass

class NMCM_A(NMCMRoot):
    def foo_bar(self):
        pass

'''
class NMCM_B(NMCMRoot):
    def fooBar(self):
        pass
'''
class MatchSignatureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith('_') or not callable(value):
                continue
            # get the prev def and compare the sig
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning('signature mismatch in %s: %s != %s',
                                    value.__qualname__, prev_sig, val_sig)

# example
class MSMRoot(metaclass=MatchSignatureMeta):
    pass

class MSM_A(MSMRoot):
    def foo(self, x, y):
        pass
    def bar(self, x, *, z):
        pass
    
class MSM_B(MSM_A):
    def foo(self, a, b):
        pass
    def bar(self, x, z):
        pass

# cookbook 9.18
# making a class manually through parts

# method
def __init__(self, name, share, price):
    self.name = name
    self.share = share
    self.price = price

def cost(self):
    return self.share * self.price

cls_dict = {
        '__init__' : __init__,
        'cost' : cost,
        }

# made a class
Stock2 = types.new_class('Stock2', 
                         (), 
                         {'metaclass': abc.ABCMeta}, 
                         lambda ns: ns.update(cls_dict))
Stock2.__module__ = __name__

# making a class using named tuple and frame hack
def named_tuple(classname, fieldname):
    # populate a dictionary of field property accessors
    cls_dict = {name: property(operator.itemgetter(n))
                for n, name in enumerate(fieldname)}
    
    # make a __new__ function and add to class dict
    def __new__(cls, *args):
        if len(args) != len(fieldname):
            raise TypeError('expect {} arguments'.format(len(fieldname)))
        return tuple.__new__(cls, args)
    
    cls_dict['__new__'] = __new__
    
    # make the class
    cls = types.new_class(classname,
                          (tuple,),
                          {},
                          lambda ns: ns.update(cls_dict))
    
    # set the module to that of the caller
    cls.__module = sys._getframe(1).f_globals['__name__']
    return cls
    
# initiate class members when define
class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(cls._fields):
            setattr(cls, name, property(operator.itemgetter(n)))

class StructTuple(tuple, metaclass= StructTupleMeta):
    _fields = []
    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError('expect {} arguments'.format(len(cls._fields)))
        return super().__new__(cls, args)

class Stock3(StructTuple):
    _fields = ['name', 'share', 'price']

class Point(StructTuple):
    _fields = ['x', 'y']

# cookbook 9.21
# avoid duplicated type check

def typed_property(name, expected_type):
    storage_name = '_' + name
    
    @property
    def prop(self):
        return getattr(self, storage_name)
    
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be {}'.format(name, expected_type))
        setattr(self, storage_name, value)
    
    return prop

# example
class Person:
    name = typed_property('name', str)
    age = typed_property('age', int)
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

# cookbook 8.14
# customized container
class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []
        
    # required sequence methods
    def __getitem__(self, index):
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
    
    # method for adding item to right location
    def add(self, item):
        bisect.insort(self._items, item)

# cookbook 8.15
# proxy and delegate
# basic structure
class Delegate_From:
    def foo(self, x):
        print(self.__class__)
        pass
    
    def bar(self):
        print(self.__class__)
        pass

class Delegate_To:
    def __init__(self):
        self._a = Delegate_From()
        
    def spam(self):
        pass
    
    def __getattr__(self, name):
        return getattr(self._a, name)

# a proxy class that wraps around another obj, 
# but only exposes its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj
        
    # delegate attr lookup to internal obj
    def __getattr__(self, name):
        print('getting attr:', name)
        return getattr(self._obj, name)
    
    # delegate attr assignment
    def __setattr__(self, name, value):
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            print('setting attr:', name, value)
            setattr(self._obj, name, value)
    
    # delegate attr deletion        
    def __delattr__(self, name):
        if name.startswith('_'):
            super().__delattr__(name)
        else:
            print('deleting attr:', name)
            delattr(self._obj, name)

# cookbook 8.17
# de-serializing
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d

# cookbook 8.18
# Mixin        