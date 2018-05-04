"""
rotate a to the right by k steps
"""


def r0(a, k):
    """
    reindexing with (i+k)%n
    """
    r = []
    n = len(a)
    for i in range(n):
        r.append(a[(i+k+1) % n])
    return r


def r1(a, k):
    """
    the stupiest way
    T(n): O(nk)
    """
    a = a[:]
    n = len(a)
    # repeat k times:
    for i in range(k):
        t = a[-1]
        for j in range(n-1, 0, -1):
            a[j] = a[j-1]
        a[0] = t
    return a


def r2(a, k):
    """
    recursive, edit inplace
    T(n): O(n)
    """
    a = a[:]

    def r_(a_, a, b):
        while a < b:
            a_[a], a_[b] = a_[b], a_[a]
            a += 1
            b -= 1

    n = len(a)
    k = k % n
    r_(a, 0, n-k-1)
    r_(a, n-k, n-1)
    r_(a, 0, n-1)
    return a


def r3(a, k):
    """
    split at pos#k and swap halves
    a shorter ver. of r0
    """
    n = len(a)
    k = k % n
    return a[n-k:] + a[:n-k]


a = [1, 2, 3, 4, 5]
r = [4, 5, 1, 2, 3]
k = 2

assert r0(a, k) == r
assert r1(a, k) == r
assert r2(a, k) == r
assert r3(a, k) == r
