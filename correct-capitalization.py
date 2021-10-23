class Solution:
    def check(self, s: str):
        case = False
        counter = 1
        if s[0].isupper():
            case = s[1].isupper()
            counter = 2
        while counter < len(s):
            if s[counter].isupper() != case:
                return False
            counter +=1
        return True

Solution = Solution()
print(Solution.check("USA"))
print(Solution.check("Calvin"))
print(Solution.check("compUter"))
print(Solution.check("coding"))