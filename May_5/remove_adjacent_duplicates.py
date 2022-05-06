from collections import deque

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:

        tmp = [["$",0]]
        for i in s:
            if tmp[-1][0] != i:
                tmp.append([i,1])
            else:    
                if tmp[-1][1] == k-1:
                    tmp = tmp[:-1]
                else:
                    tmp[-1][1] += 1
        
        return "".join([x * y for x,y in tmp])
