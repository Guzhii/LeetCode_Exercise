import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        
        tmp = [-x for x in target]
        heapq.heapify(tmp)
        
        while True:
            top = - heapq.heappop(tmp)
            bot = 2 * top - s
            if bot < 1 or bot > top:
                return False
            s = s - top + bot
            heapq.heappush(tmp, -bot)
            if all(x == -1 for x in tmp):
                return True
