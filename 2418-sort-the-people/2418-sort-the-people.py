import operator
from collections import defaultdict

class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        # d=defaultdict(list)
        # for k,v in names, heights:
        #     d[k].append(v)
        # print(d)
        # dict1 = dict(zip(names, heights))
        # print(dict1)
        # sorted_dict = sorted(dict1.items(), key=lambda x:x[1], reverse = True)
        # print(sorted_dict)
        
        # return [tup[0] for tup in sorted_dict]
        
        l=[]
        for i in range(len(heights)):
            l.append([heights[i],names[i]])
        l.sort(reverse=True)
        k=[]
        for i in l:
            k.append(i[1])
        return k