from collections import defaultdict

"""
del occurence > n
e.g. [1,2,3,1,2,1] => [1,2,3]
"""


def del_nth(i_arr, n):
    """
    parm:
        i_arr: input, assume it's 1d
        n: repeat
    ret:
        res
    """
    cnt = defaultdict(int)
    res = []
    for el in i_arr:
        if cnt[el] < n:
            res.append(el)
            cnt[el] += 1
    return res
