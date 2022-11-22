class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        arr = []
        l = 0
        r = n
        while r < len(nums):
            arr.append(nums[l])
            l+=1
            arr.append(nums[r])
            r+=1
            
        return arr