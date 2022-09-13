# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        retNode = ListNode(None, None)
        ptr = retNode
        
        if list1 == None and list2 != None :
            ptr.next = list2
        if list2 == None and list1 != None:
            ptr.next = list1
            
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                if ptr == None:
                    ptr = ListNode(list1.val, None)
                else:
                    ptr.next = ListNode(list1.val, None)
                    
                ptr = ptr.next
                list1 = list1.next
            else:
                if ptr == None:
                    ptr = ListNode(list2.val, None)
                else:
                    ptr.next = ListNode(list2.val, None)
                ptr = ptr.next
                list2 = list2.next
                
            if list1 == None and list2 != None :
                ptr.next = list2
            if list2 == None and list1 != None:
                ptr.next = list1
        return retNode.next
                
                
                
                
        
