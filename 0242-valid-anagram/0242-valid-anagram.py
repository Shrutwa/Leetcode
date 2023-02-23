class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1 = list(s)
        l1.sort()
        l2 = list(t)
        l2.sort()
        
        if l1 == l2:
            return True
        
        return False
        