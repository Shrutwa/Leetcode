# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # du
        # print(head)
        # head = head.next
        # print(head)
        dummy = head        
        i = 1
        l=0
        while head.next != None:          
            
            i+=1
            head = head.next
            l=i/2
            
            
        for i in range(l):
            dummy = dummy.next
        
        return dummy
         
    
        
        