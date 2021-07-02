# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA = 0
        lenB = 0
        tempA = headA
        tempB = headB
#--------------- GET LENGTH
        while tempA != None:
            lenA += 1
            tempA = tempA.next
            
        while tempB != None:
            lenB += 1
            tempB = tempB.next
#--------------- ADJUST LONGER LINKEDLIST
        tempA = headA
        tempB = headB
        toGo = 0
        if lenA > lenB:
            toGo = lenA - lenB
            for i in range(toGo):
                tempA = tempA.next
            #print(tempA)
            
        if lenB > lenA:
            toGo = lenB - lenA
            for i in range(toGo):
                tempB = tempB.next
            #print(tempB)
            
#--------------- ITERATE THROUGH BOTH TO GET INTERSECTION
        while tempA != None and tempB != None:
            if tempA == tempB:
                return tempA #or tempB
            tempA = tempA.next
            tempB = tempB.next

            
            
        
                
            
            
