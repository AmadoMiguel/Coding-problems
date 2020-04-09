# Given an array of strings s, find the number of common characters shared by all of the strings.
#
# Example
#
# For s = ["aabcc", "adcaa", "acdba"], the output should be
# commonCharacterCount2(s) = 3.
#
# There are 3 common characters in these strings: two as and one c.


def mM(m1,m2):
    for k in m1.keys():
        if k in m2.keys():
            m1[k]=min(m1[k],m2[k])
        else:
            m1[k] = 0
    return m1


def commonCharacterCount2(s):
    if len(s) == 1:
        return len(s[0])
    sL,hM=len(s),{}
    for l in s[0]:
        hM[l]=hM.setdefault(l,0)+1
    for w in s[1:]:
        a = {}
        for l in w:
            a[l]=a.setdefault(l,0)+1
        hM = mM(hM,a)
    return sum([n for n in hM.values()])


assert commonCharacterCount2(["aabcc", "adcaa", "acdba"]) == 3
