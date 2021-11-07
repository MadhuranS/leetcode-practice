class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict = collections.Counter(s1)
        if len(s1) > len(s2):
            return False
        windowend = len(s1) - 1
        windowstart = 0
        newdict = collections.Counter(s2[windowstart:windowend + 1])
        if newdict == dict:
            return True
        for i in range(0, len(s2) - len(s1)):
            if newdict[s2[windowstart]] == 1:
                newdict.pop(s2[windowstart])
            else:
                newdict[s2[windowstart]] -= 1
            windowend += 1
            windowstart += 1
            newdict[s2[windowend]] = newdict.get(s2[windowend], 0) +1
            if newdict == dict:
                return True

        return False