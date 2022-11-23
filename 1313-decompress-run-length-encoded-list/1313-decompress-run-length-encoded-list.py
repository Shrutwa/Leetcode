class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(1,len(nums),2):
            a.extend([nums[i]]*nums[i-1])
        return a
        