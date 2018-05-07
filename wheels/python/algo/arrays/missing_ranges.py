"""
pre-cond: array should be in order
elements in array is like cuts, will be excluded in returns
"""


def mr(a, p, q):
    """
    in:
        a: sorted 1d array
        p: low end
        q: high end
    ou:
        r: list of range tuples
    """
    r = []
    s = p
    a = sorted(a)
    if a == []:
        return [(p, q)]
    for i in a:
        if s == i:
            # bypassing the cut
            s += 1
        # elif i > s:
        else:
            r.append((s, i-1))
            # bypassing the cut
            s = i + 1

    # dealing the tailing range
    if s <= q:
        r.append((s, q))

    return r
