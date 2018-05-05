from collections import Iterable

"""
turn nested iterable to flatten
"""


"""
called
"""


def f_(i, o=None):
    """
    in:
        i: input
        o: output
    ou:
        1d list
    """
    if o is None:
        o = []
    for el in i:
        if isinstance(el, Iterable):
            f_(el, o)
        else:
            o.append(el)
    return o


"""
caller
"""


def f(it):
    """
    in:
        it: any iterable of any dim
    ou:
        generator of 1d
    """
    for el in it:
        if isinstance(el, Iterable):
            yield from f_(el)
        else:
            yield el
