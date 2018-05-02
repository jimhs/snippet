"""
turn nested iterable to flatten
"""
from collections import Iterable

"""
called
"""


def flatten_(i_arr, o_arr=None):
    """
    parm:
        i_arr: input
        o_arr: output
    ret:
        1d list
    """
    if o_arr is None:
        o_arr = []
    for el in i_arr:
        if isinstance(el, Iterable):
            flatten_(el, o_arr)
        else:
            o_arr.append(el)
    return o_arr


"""
caller
"""


def flatten(it):
    """
    parm:
        it: any iterable of any dim
    ret:
        generator of 1d
    """
    for el in it:
        if isinstance(el, Iterable):
            yield from flatten_(el)
        else:
            yield el
