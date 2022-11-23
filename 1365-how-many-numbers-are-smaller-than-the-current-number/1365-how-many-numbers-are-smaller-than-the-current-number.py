class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l1 = sorted(nums)
        return [l1.index(i) for i in nums]