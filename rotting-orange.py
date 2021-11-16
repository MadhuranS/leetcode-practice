class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        queue = []
        fresh = set()
        visited = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i,j))
                    visited.add((i, j))
                if grid[i][j] == 1:
                    fresh.add((i, j))

        if not(queue) and not(fresh):
            return 0
        if not(queue) and fresh:
            return -1
        count = 0
        while queue:
            
            size = len(queue)
            
            for i in range(size):
                x, y = queue.pop(0)
                
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    newx = x + dx
                    newy = y + dy
                    if not(newx < 0 or newx >= r or newy < 0 or newy >= c or (newx, newy) in visited or grid[newx][newy] == 0):
                        queue.append((newx, newy))
                        visited.add((newx, newy))
                        fresh.remove((newx, newy))
            count += 1
            
            
        if fresh:
            return -1
        else:
            return count - 1
                
                
                        