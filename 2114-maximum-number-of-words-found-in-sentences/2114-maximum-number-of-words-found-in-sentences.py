class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        cnt = 0
        arr = []
        for s in sentences:
            cnt=0
            for i in range(0, len(s)):
                if s[i] == " ":
                    cnt += 1
                    
            arr.append(cnt+1)
            
        return max(arr)