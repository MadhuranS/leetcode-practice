class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rowdict = {}
        
        if numRows == 1:
            return s
        
        for i in range(numRows):
            rowdict[i] = []
        
        count = 0
        directionDown = True
        for char in s:
            rowdict[count].append(char)
            if count == numRows - 1:
                directionDown = False
            if count == 0:
                directionDown = True
            if directionDown:
                count += 1
            else:
                count -= 1
        
        ans = ""
        for key, value in rowdict.items():
            ans += "".join(value)
        print(ans)
        return ans