class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
 
    #Brute force
#         count = 0
#         for i in range(0,len(nums)):
#             for j in range(i+1,len(nums)+1):
#                 s = 0
#                 for l in range(i,j):
#                     s+=nums[l]
#                 if s == k:
#                     count+=1
                    
#         return count

    #Cummulative Sum
#             count = 0
#             s = [0]*(len(nums)+1)
#             s[0]=0
#             for i in range(1, len(nums)+1):
#                 s[i]=s[i-1]+nums[i-1]
#             for i in range(0,len(nums)):
#                 for j in range(i+1,len(nums)+1):
#                     if(s[j]-s[i]==k):
#                         count+=1
                        
#             return count

    #HashMap
        count = 0
        sumdict = {0:1}
        s = 0
        for num in nums:
            s+=num
            if s-k in sumdict:
                count+=sumdict[s-k]
            if s in sumdict:
                sumdict[s]+=1
            else:
                sumdict[s]=1
        return count
              
         
        
