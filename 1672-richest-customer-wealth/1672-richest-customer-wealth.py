class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l1 = []
        for i in accounts:
            l1.append(sum(i))
            
        return max(l1)
            