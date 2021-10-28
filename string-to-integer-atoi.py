class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        test = "3"
        whitespacecheck = True
        while whitespacecheck and i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                whitespacecheck = False
        coefficient = 1
        if i >= len(s):
            return 0
        if s[i] == "-":
            coefficient = -1
            i += 1
        elif s[i] == "+":
            i += 1
        
        if i >= len(s) or not(s[i].isdigit() ):
            return 0
        num = 0
        while i < len(s):
            if not(s[i].isdigit()):
                return num * coefficient
            num = num * 10 + int(s[i])
            i += 1
            if -2**31 > num * coefficient:
                return -2**31
            elif num * coefficient > 2**31 - 1:
                return 2**31 - 1
        return num * coefficient