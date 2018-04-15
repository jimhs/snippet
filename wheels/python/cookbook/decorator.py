#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:12:35 2018

@author: jimhs
"""

import time
import types

import logging
#logging.basicConfig(level=logging.DEBUG)

from functools import wraps, partial
from inspect import signature, Parameter
from contextlib import contextmanager


def timethis(func):
    '''
    decorator that report the execute time
    '''
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper

# cookbook 9.22
# easy way to use contextmanager
@contextmanager
def timethis2(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('{}: {}'.format(label, end-start))

# example
with timethis2('counting'):
    n = 100
    while n >= 0:
        n -= 1

# advanced use of contextmanager
@contextmanager
def list_transaction(orig_list):
    working = list(orig_list)
    yield working
    orig_list[:] = working
    
def deco2(func):
    '''
    decorator that report the execute time
    '''
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        print('deco 2')
        return func(*args, **kwargs)
    return wrapper

# utility deco to attach a function as attr of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

# cookbook 9.5
def logged(level, name=None, message=None):
    '''
    add logging to function
    '''
    
    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)
        
        # attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel
            
        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg
            
        return wrapper    
    return decorator

# cookbook 9.6
def logged2(func=None, *, level=logging.WARNING, name=None, message=None):        
    '''
    add logging to function
    '''
    
    if func is None:
        return partial(logged2, level=level, name=name, message=message)
    
    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)     
    return wrapper

# cookbook 9.11
def optional_debug(func):
    sig = signature(func)
    if 'debug' in sig.parameters:
        raise TypeError('debug already defined')
        
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('calling', func.__name__)
        return func(*args, **kwargs)
    
    parms = list(sig.parameters.values())
    parms.append(Parameter('debug', Parameter.KEYWORD_ONLY, default=False))
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
    
# cookbook 9.7
def type_assert(*ty_args, **ty_kwargs):
    def decorator(func):
        # if in optimized mode, disable type checking
        # >>> python -O | -OO
        if not __debug__:
            return func
        
        # map function arg names to supplied type
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # enforce type asserting across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                            'argument {} must be {}'.format(name, bound_types[name])
                            )
            return func(*args, **kwargs)     
        return wrapper
    return decorator

# cookbook 8.9
# descriptor for a type-checked attribute
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError('expect ' + str(self.expected_type))
        instance.__dict__[self.name] = value
        
    def __del__(self, instance):
        del instance.__dict__[self.name]

# cookbook 8.9
# class deco that applies it to selected attribute
# @type_assert2(name=str, share=int, price=float)
def type_assert2(**kwargs):
    def deco(cls):
        for name, expected_type in kwargs.items():
            # attach a typed descriptor to class
            setattr(cls, name, Typed(name, expected_type))
        return cls
    return deco

# cookbook 8.10
# lazy and cached property, mutable
class LazyProperty:
    def __init__(self, func):
        self.func = func
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value

# imutable version
def lazyproperty(func):
    name = '_lazy_' + func.__name__
    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value
        return lazy
    
# cookbook 9.8
class DecoCls:
    # deco as an instance method
    def deco1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('deco1 as instance')
            return func(*args, **kwargs)
        return wrapper
    
    # deco as classmethod
    @classmethod
    def deco2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print('deco2 as classmethod')
            return func(*args, **kwargs)
        return wrapper

# cookbook 9.9
class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0
        
    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)
    
    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)

# cookbook 9.12
# print function repeat itself, why?
def log_attribute(cls):
    # save the original
    orig_getattribute = cls.__getattribute__
    
    # define new
    def new_attribute(self, name):
        #print('getting:', name)
        return orig_getattribute(self, name)
    
    # attach to the class and return
    cls.__getattribute__ = new_attribute
    return cls


@log_attribute
class LA:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def spam(self):
        pass

# cookbook 9.12
# solution 2
#??? print function repeat itself, why
class LoggedGetattribute:
    def __getattribute__(self, name):
        print('getting:', name)
        return super().__getattribute__(name)
    
class LA2(LoggedGetattribute):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def spam(self):
        pass
    
@timethis
@deco2
def countdown(n:int):
    '''
    count down
    
    >>> countdown(10000)
    deco 2
    countdown 0.0008087158203125
    '''
    while n > 0:
        n -= 1

# cookbook 9.10
# class illustrating deco applied to different methods
class CountDown:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1
            
    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1

@logged2(level=logging.CRITICAL, name='critical example')
def add(x,y):
    return x + y

@type_assert(int, z=int)
def spam(x, y, z=42):
    print(x, y, z)

decocls = DecoCls()

@decocls.deco1
def grok1():
    pass

@DecoCls.deco2
def grok2():
    pass

@Profiled
def foo(x, y):
    return x - y

class Bar:
    @Profiled
    def bar(self, x):
        print(self, x)


        