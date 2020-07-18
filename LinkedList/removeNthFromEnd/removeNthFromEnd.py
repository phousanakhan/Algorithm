# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp = head
        if n == 0 or head is None:
            return(head)
        
        while temp is not None:
            length += 1
            temp = temp.next
            
        target = length - n
        count = 0
        toRemove = None
        preMove = None
        temp1 = head
        
        while count != target:
            preMove = temp1
            temp1 = temp1.next
            toRemove = temp1
            count += 1
        
        if preMove == None: #remove first node in the list
            return(head.next)
        else:
            preMove.next = toRemove.next #3->4->5. preMove.next = 4 = toRemove.next = 5. Thus, 3->5
            toRemove.next = None #remove the connection from 4->5
            return(head)
        