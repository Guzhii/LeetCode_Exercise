import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        
        def lastDay(x):
            return x[1]
        
        courses.sort(key=lastDay)
        
        total = 0
        tmp = []
        for c in courses:
            total += c[0]
            heapq.heappush(tmp, -c[0])
            if total > c[1]:
                t_pop = heapq.heappop(tmp)
                total += t_pop
        
        return len(tmp)
