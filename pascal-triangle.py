class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        for i in range(numRows):
            arr.append([1] * (i + 1))
            
        for i in range(numRows):
            for j in range(1, i):
                arr[i][j] = arr[i-1][j - 1] + arr[i-1][j]
        return arr