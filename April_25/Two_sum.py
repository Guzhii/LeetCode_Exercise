class Solution(object):
    def twoSum(self, nums, target):
        for n in nums:
            x = target - n
            if x != n:
                if x in nums:
                    return [nums.index(n), nums.index(x)]
            else:
                tmp_nums = nums.copy()
                tmp_nums.remove(x)
                if x in tmp_nums:
                    return [nums.index(n), tmp_nums.index(x)+1]
