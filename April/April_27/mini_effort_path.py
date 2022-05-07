from queue import PriorityQueue

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights) - 1
        c = len(heights[0]) - 1

        ans = 0
        q = PriorityQueue()
        q.put((0,0,0))
               
    
        while True :
            dif, y, x = q.get()
            h = heights[y][x]
            if h == 0 : continue                         
            ans = max(ans, dif)
      
            if y == r and x == c : break 
            
            tmp = [(1,0),(-1,0),(0,1),(0,-1)]
            
            for dx,dy in tmp:
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x <= c and 0 <= new_y <= r and heights[new_y][new_x] != 0:
                    q.put((abs(h - heights[new_y][new_x]), new_y, new_x))
        
            heights[y][x] = 0
    
        return ans
