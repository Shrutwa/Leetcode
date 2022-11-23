class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        dict1 = {'type': 0, 'color':1, 'name':2} 
        cnt = 0
        for i in items:
            if i[dict1[ruleKey]]==ruleValue:
                cnt+=1
                
        return cnt
                
        