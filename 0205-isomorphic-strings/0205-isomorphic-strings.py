class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = set(s)
        # print(s1)
        s2 = set(t)
        # print(s2)
        z = zip(s,t)
        sz = set(z)
        # print(sz)
        
        return (len(s1) == len(s2) == len(sz))