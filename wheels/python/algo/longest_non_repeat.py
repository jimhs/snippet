"""
longest substr w/o repeating chars

todo@may.02: why 'for' loop not working?
"""


def lnr(s):
    """
    in:
        s: a string
    ou:
        ss: lnr
    """
    i = 0
    ss = []
    u = []
    while i < len(s):
        # no need to use set(u)
        if s[i] not in u:
            u.append(s[i])
            i = i + 1
            continue
        if len(u) > len(ss):
            ss = u[:]
            u = []
    return "".join(ss)


assert lnr('pwwkew') == 'wke'
