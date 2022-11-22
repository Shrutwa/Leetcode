class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=1
        cnt=0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    cnt+=1
                
            j+=1
        i+=1
        
        return cnt