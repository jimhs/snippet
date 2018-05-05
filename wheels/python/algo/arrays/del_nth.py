from collections import defaultdict

"""
del occurence > n
e.g. [1,2,3,1,2,1] => [1,2,3]
T(n): O(n)
"""


def dn(a, n):
    """
    in:
        a: 1d arr
        n: repeats
    ou:
        r
    """
    i = defaultdict(int)
    r = []
    for el in a:
        if i[el] < n:
            r.append(el)
            i[el] += 1
    return r
