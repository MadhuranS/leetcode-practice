class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = []
        visited = set()
        r = len(mat)
        c = len(mat[0])
        ans = [[0]*c]*r
        for i in range(r):
            for j in range(c):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
                    
        count = 0
        print(visited)
        while queue:
            size = len(queue)
            for i in range(size):
                x, y = queue.pop(0)
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    newx = x + dx
                    newy = y + dy
                    if not(newx >= r or newx < 0 or newy >= c or newy < 0 or (newx, newy) in visited):
                        queue.append((newx, newy))
                        visited.add((newx, newy))
                mat[x][y] = count
            count += 1
        
        
        
  
        return mat