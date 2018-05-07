"""
pre-cond: input array is sorted and w/o dup
"""


def sr(a):
    """
    in:
        a: 1d array
    ou:
        list of range tupples
    """
    r = []
    i = 0
    # enter loop directly, no need to worry 1-el list
    while i < len(a):
        n = a[i]
        # w/i boundary and in sequence
        while i + 1 < len(a) and a[i + 1] - a[i] == 1:
            i += 1
        if a[i] != n:
            r.append((n, a[i]))
        else:
            r.append((n, n))
        i += 1
    return r
