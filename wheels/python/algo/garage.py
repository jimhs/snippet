"""
steps at most: n+1. '+1' is the additional step for two 0s overlapped
[0, 1, 2, 3, 4]
[0, 4, 3, 2, 1]
otherwise： n. 'n' is total len
[1, 0, 2, 3, 4]
[0, 4, 3, 2, 1]
"""


def g(a, b):
    """
    in:
        a: initial lineup
        b: final lineup
    ou:
        s: total steps
        q: list of [ status ]
    """
    a = a[:]
    s = 0
    q = []
    # loop till b reached
    while a != b:
        # get pos# of 0 fr a
        z = a.index(0)
        # either two 0s not overlapped
        if z != b.index(0):
            # get target fr b
            v = b[z]
            # get pos# of target fr a
            u = a.index(v)
            # swap 0 <-> target in a
            a[z], a[u] = a[u], a[z]
        # or two 0s overlapped
        else:
            # iter thru a
            for i in range(len(a)):
                # till 1st not overlapped target
                if a[i] != b[i]:
                    # swap 0 <-> target in a
                    a[z], a[i] = a[i], a[z]
                    break
        # add new a to q
        q.append(a[:])
        # s + 1
        s += 1
    return s, q
