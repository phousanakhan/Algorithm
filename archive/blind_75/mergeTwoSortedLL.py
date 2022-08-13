# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        ptr = dummy
        
        while (True):
            if list1 == None and list2 == None:
                break
            elif list1 == None:
                ptr.next = list2
                break
            elif list2 == None:
                ptr.next = list1
                break
            else:
                #increament ptr of smaller val
                if list1.val < list2.val:
                    smallerVal = list1.val
                    list1 = list1.next
                else:
                    smallerVal = list2.val
                    list2 = list2.next
                newNode = ListNode(smallerVal)
                ptr.next = newNode
                ptr = ptr.next
            
        
        return dummy.next
