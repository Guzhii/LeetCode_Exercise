class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dif = [(1,0),(-1,0),(0,1),(0,-1)]
        
        @lru_cache(None)
        def dfs(x, y):
            ans = 1
            for dx,dy in dif:
                if 0 <= x+dx < m and 0 <= y+dy < n:
                    if matrix[x+dx][y+dy] > matrix[x][y]:
                        tmp = dfs(x+dx, y+dy)+1
                        ans = max(ans, tmp)
            return ans
        
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,dfs(i, j))
                
        return ans
