from bisect import bisect_left


"""
method 1: traversal fr left
method 2: combine two_sum
"""


def ths(a, t):
    """
    in:
        a: list(int)
        t: sum
    ou:
        set(touple(int, int, int))
    """
    rs = set()
    a.sort()
    n = len(a)
    s = bisect_left(a, t)
    # this boundary tests ok, is it fine?
    for i in range(s):
        if i > 0 and a[i] == a[i - 1]:
            continue
        # flake8 dont allow naming it 'l', but 'r' ok
        lf, r = i + 1, n - 1
        while lf < r:
            u = a[i] + a[lf] + a[r]
            if u > t:
                r -= 1
            elif u < t:
                lf += 1
            else:
                rs.add((a[i], a[lf], a[r]))

                while lf < r and a[lf] == a[lf+1]:
                    lf += 1
                while lf < r and a[r] == a[r-1]:
                    r -= 1

                lf += 1
                r -= 1
    return rs
