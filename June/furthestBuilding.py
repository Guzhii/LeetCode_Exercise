import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        dif = []
        acc = 0
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                acc += heights[i] - heights[i-1]
                heapq.heappush(dif, heights[i-1] - heights[i])
                if acc > bricks:
                    if ladders > 0:
                        ladders -= 1
                        acc += heapq.heappop(dif)
                    else:
                        return i-1
        
        return n-1
