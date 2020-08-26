# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        try:
            lenA = 0
            lenB = 0
            tempA = headA
            tempB = headB
            while headA != None:
                headA = headA.next
                lenA += 1
            while headB != None:
                headB = headB.next
                lenB += 1
            headA = tempA
            headB = tempB

            if lenA > lenB:
                for i in range(lenA-lenB):
                    headA = headA.next
            if lenB > lenA:
                for i in range(lenB-lenA):
                    headB = headB.next

            while headA != headB:
                headA = headA.next
                headB = headB.next

            return headB #or headA
        except:
            return None
