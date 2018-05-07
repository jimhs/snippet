"""
three ways
pre-cond: only one digit per element in the input array
e.g. [1, 10, 100] won't allowed, use [1, 1, 0, ...] instead
"""


"""
simpiest
"""


def po0(a):
    for i, v in reversed(list(enumerate(a))):
        a[i] = (a[i] + 1) % 10
        if a[i]:
            return a
    # todo@may.07 [1] won't attach to a permernantly
    # a = [1] + a
    return a.insert(0, 1)


"""
a little tweaks
basically same as po0
"""


def po1(a):
    n = len(a)
    # traversal digits list fr tail to head
    for i in range(n-1, -1, -1):
        if a[i] < 9:
            a[i] += 1
            return a
        a[i] = 0
    return a.insert(0, 1)


"""
third way is not intuitive
"""


def po2(a):
    pass
