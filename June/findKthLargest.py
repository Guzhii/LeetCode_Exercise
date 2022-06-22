class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        piv = nums[0]
        pre = [x for x in nums if x < piv]
        mid = [x for x in nums if x == piv]
        pos = [x for x in nums if x > piv]
        
        p = len(pos)
        m = len(mid)

        if k <= p:
            return self.findKthLargest(pos, k)
        elif k > p + m:
            return self.findKthLargest(pre, k-m-p)
        else:
            return mid[0]
