class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(i: int, curr: List[int]):
            if len(curr) == k:
                output.append(curr[:])
            else:
                for idx in range(i, n+1):
                    curr.append(idx)
                    backtrack(idx + 1, curr)
                    curr.pop()
        output = []
        backtrack(1, [])
        return output