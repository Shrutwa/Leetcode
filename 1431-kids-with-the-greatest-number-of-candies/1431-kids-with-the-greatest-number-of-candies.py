class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        s = max(candies)
        l1=[]
        
        for i in candies:
             l1.append((i+extraCandies) >= s)
        
        return l1