"""
two sum
#todo@may.06 cant deal with input list that contain dup v.
"""


def ts(a, t):
    """
    in:
        a: list of nums
        t: sum
    ou:
        r: list of index tupple(s) that sum to t
    """
    d = {}
    r = []
    for i, v in enumerate(a):
        if v in d:
            r.append((d[v], i))
        else:
            # dup v will over-write pre v
            # e.g. [1, 1, 2, ...], 2nd '1' will over-write 1st '1'
            d[t - v] = i
    return r


a = [1, 1, 2, 3, 4]
t = 5
print(ts(a, t))
