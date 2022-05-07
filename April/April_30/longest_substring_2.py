class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        
        maxx = 0
        tmp = []
        
        for j in range(n):
            cur = s[j]
            if cur in tmp:
                tmp = tmp[tmp.index(cur)+1:]
                
            tmp.append(s[j])
            maxx = max(maxx, len(tmp))
            
        return maxx
