class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        
        maxx = 0
        tmp = {}
        
        for j in range(n):
            cur = s[j]
            if s[j] in tmp:
                i = max(i, tmp[s[j]])

            tmp[s[j]] = j+1
            maxx = max(maxx, j + 1 - i)
            
        return maxx
