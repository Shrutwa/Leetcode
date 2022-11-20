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
                
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        l1 = self.listnode_to_list(head)
        print(l1)
        res = self.list_to_listnode(l1,len(l1))
        
        return res
        
        
    
                
    