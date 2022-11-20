# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def list_to_listnode(self, pylist, link_count):
        if len(pylist) > 1:
            ret = ListNode(pylist.pop())
            ret.next = self.list_to_listnode(pylist, link_count)
            return ret
        elif len(pylist)>0:
            return ListNode(pylist.pop(), None)
        else:
            return ListNode('', None)
        
    def listnode_to_list(self, listnode):
        res_list = []
        
        if listnode == None:
            return res_list
        else: 
            while True:
                res_list.append(listnode.val)
                if listnode.next != None:
                    listnode = listnode.next
                else:
                    return res_list
    
            
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        print(list1)
        print(list2)
            
        l1 = []
        l2 = []
        sorted_list = []
        
        
        l1 = self.listnode_to_list(list1)
        l2 = self.listnode_to_list(list2)
        
        # print(type(l1))
        # print(type(l2))
        
        
        sorted_list = sorted(l1 + l2, reverse=True)
        ret_list = self.list_to_listnode(sorted_list,len(sorted_list))
        
        return ret_list
        
        