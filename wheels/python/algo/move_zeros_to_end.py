"""
use a parallel list to recieve results
"""


def ze(s):
    z = 0
    r = []
    for i in s:
        if i is 0:
            z += 1
        else:
            r.append(i)
    r.extend([0] * z)
    return r
