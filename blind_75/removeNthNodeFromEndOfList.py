# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        countHead = head
        while countHead != None:
            length += 1
            countHead = countHead.next
            
        target = length - n
        count = 0
        tempHead = head
        curHead = None
        curHeadNext = None
        while count != target:
            curHead = tempHead
            tempHead = tempHead.next
            curHeadNext = tempHead
            count += 1
            
        if curHead == None:
            return head.next
        else:
            curHead.next = curHeadNext.next
            return head
            
            
            
        

            

            
            
        
