class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        tmp = {}
        res = 0
        for i in nums:
            if k-i in tmp and tmp[k-i] != 0:
                tmp[k-i] -= 1
                res += 1
            elif i not in tmp:
                tmp[i] = 1
            else:
                tmp[i] += 1
                
        return res
