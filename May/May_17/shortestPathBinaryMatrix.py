class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        dif = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = set()
        q = deque()
        q.append((0,0,1))
        
        if grid[0][0] == 1 or grid[N-1][N-1] == 1:
            return -1
        
        while q:
            x, y, n = q.popleft()
            if x == N-1 and y == N-1:
                return n
            for dx,dy in dif:
                x_new = x+dx
                y_new = y+dy
                if 0 <= x_new < len(grid) and 0 <= y_new < len(grid[0]) and grid[x_new][y_new] == 0 and (x_new, y_new) not in visited:
                    q.append((x_new, y_new,n+1))
                    visited.add((x_new, y_new))
        
        return -1
