class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [[]]
        
        for char in s:
            n = len(ans)
            if char.isdigit():
                for i in range(n):
                    ans[i].append(char)
            else:
                for i in range(n):
                    ans.append(ans[i][:])
                    ans[i].append(char.upper())
                    ans[n + i].append(char.lower())

        return map("".join, ans)