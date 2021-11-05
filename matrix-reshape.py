class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

       
        if not(r * c == len(mat) * len(mat[0])):
            return mat
    
        ans = [[]]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if len(ans[-1]) == c:
                    ans.append([mat[i][j]])
                else:
                    ans[-1].append(mat[i][j])
        return ans