class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        l = zip(s,indices)
        str = ''
        for i in range(0, len(l)):
            for j in range(0, len(l)-i-1):
                if (l[j][1] > l[j + 1][1]):
                    temp = l[j]
                    l[j]= l[j + 1]
                    l[j + 1]= temp
        
        result = [t[0] for t in l]
        str = ''.join(result)
        
        return str
