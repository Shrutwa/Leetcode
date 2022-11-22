class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        s1 = set(allowed)
        cnt=0
        
        for w in words:
            s2 = set(w)
            if s2.issubset(s1):
                cnt+=1
        return cnt