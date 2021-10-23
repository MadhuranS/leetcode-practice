class Solution:
    def routeCheck(self, s: str):
        pos = [0,0]
        for char in s:
            x = pos[0]
            y = pos[1]
            if char == 'L': 
                pos = [x - 1, y]
            elif char == 'R':
                pos = [x + 1, y]
            elif char == 'D':
                pos = [x, y-1]
            else:
                pos = [x, y+1]
        if pos[0] == 0 and pos[1] == 0:
            return True
        return False

Solution = Solution()
print(Solution.routeCheck("LR"))
print(Solution.routeCheck("URURD"))
print(Solution.routeCheck("RUULLDRD"))