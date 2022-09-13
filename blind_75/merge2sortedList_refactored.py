# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        retNode = ListNode(None)
        ptr = retNode
        
        while(True):
            if list1 == None and list2 == None:
                break
            elif list1 != None and list2 == None:
                ptr.next = list1
                break
            elif list1 == None and list2 != None:
                ptr.next = list2
                break
            else:
                if list1.val < list2.val:
                    ptr.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    ptr.next = ListNode(list2.val)
                    list2 = list2.next
                ptr = ptr.next
                    
        return retNode.next
