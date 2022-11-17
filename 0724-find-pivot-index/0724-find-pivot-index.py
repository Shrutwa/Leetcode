class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_sum = 0
        r_sum = sum(nums)
        for i in range(len(nums)):
            r_sum -= nums[i]
            if l_sum == r_sum:
                return i
            l_sum += nums[i]
        return -1