class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        x = -1
        y = -2
        
        nums_s = nums.copy()
        nums_s.sort()
        
        for i in range(n):
            if nums[i] != nums_s[i]:
                if x == -1:
                    x = i
                else:
                    x = min(x, i)
                
                y = max(y, i)
        
        return y - x + 1
        
