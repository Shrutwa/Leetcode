class Solution(object):
    def runningSum(self, nums):
        r_sum = []
        s = 0
        for i in nums:
            s=s+i
            r_sum.append(s)

        return r_sum