import copy
def isLegal(s):
    for i in range(len(s - 2)):
        if abs(ord(s[i]) - ord(s[i + 1])) == 1:
            return False
    return True

def makeLegalSrings(s):
    return makeLegalStringsH(s)

def makeLegalStringsH(ns, i = 1):
    s = copy.copy(ns)
    if len(s) == 1:
        return s
    else:
        for j in range(len(s[i:])):
            s[i], s[j] = s[j], s[i]
            if isLegal(s[:i]):
                s = s[:i] + makeLegalStringsH(s[i:])
                return s
            s[i], s[j] = s[j], s[i]
        return None

print(makeLegalSrings('abcd'))