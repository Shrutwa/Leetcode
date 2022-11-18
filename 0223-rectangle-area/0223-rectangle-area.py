class Solution(object):
    def computeArea(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        """
        :type ax1: int
        :type ay1: int
        :type ax2: int
        :type ay2: int
        :type bx1: int
        :type by1: int
        :type bx2: int
        :type by2: int
        :rtype: int
        """
        l1 = abs(ax1-ax2)
        b1 = abs(ay1-ay2)
        l2 = abs(bx1-bx2)
        b2 = abs(by1-by2)
        a1 = l1*b1
        a2 = l2*b2
       
        
        return a1+a2 - max(min(ax2,bx2)-max(ax1,bx1), 0) * max(min(ay2,by2)-max(ay1,by1), 0)
        