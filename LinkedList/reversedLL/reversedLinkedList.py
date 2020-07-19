# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head != None:
            currentNode = head
            head = head.next
            currentNode.next = prev
            prev = currentNode
        return(prev)