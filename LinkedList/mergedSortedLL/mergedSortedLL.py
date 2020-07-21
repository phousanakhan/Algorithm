# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        ptr = dummy
        
        while(1):
            if l1 == None and l2 == None:
                break
            elif l1 == None:
                ptr.next = l2
                break
            elif l2 == None:
                ptr.next = l1
                break
            else:
                smallerVal = 0
                if l1.val < l2.val:
                    smallerVal = l1.val
                    l1 = l1.next
                else:
                    smallerVal = l2.val
                    l2 = l2.next
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr = ptr.next
        return(dummy.next)