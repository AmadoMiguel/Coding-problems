# You are given an array of desired filenames in the order of their creation. Since two files cannot have equal
# names, the one which comes later will have an addition to its name in a form of (k), where k is the smallest
# positive integer such that the obtained name is not used yet.
#
# Return an array of names that will be given to the files.

# For names = ["doc", "doc", "image", "doc(1)", "doc"], the output should be
# fileNaming(names) = ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"].


def nF(nn, fs, hm):
    aP = False
    cN = 1
    while nn in hm.keys():
        if not aP:
            nn += "("+str(cN)+")"
            aP = True
        else:
            lP = len(nn) - 1 - nn[::-1].find("(")
            subS = nn[lP:]
            subS = subS.replace(subS[1:-1], str(int(cN)))
            nn = nn[:lP] + subS
            cN += 1
    return nn


def fileNaming(names):
    ns,hm = [],{}
    for n in names:
        s = nF(n, ns, hm)
        hm[s] = 0
        ns.append(s)
    return ns


names = ["doc", "doc", "image", "doc(1)", "doc"]
assert fileNaming(names) == ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]  # True
names = ["dd","dd(1)","dd(2)","dd","dd(1)","dd(1)(2)","dd(1)(1)","dd","dd(1)"]
assert fileNaming(names) == ["dd","dd(1)","dd(2)","dd(3)","dd(1)(1)","dd(1)(2)","dd(1)(1)(1)","dd(4)","dd(1)(3)"]
