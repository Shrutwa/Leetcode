class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ''
        
        strs.sort()
        
        for char in range(len(strs[0])):
            if strs[0][char]==strs[-1][char]:
                res +=strs[0][char]
                continue
            else :
                break
                
        return res