# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        array1 = []
        array2 = []
        while l1 != None:
            array1.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            array2.append(str(l2.val))
            l2 = l2.next
            
        array1 =  ''.join(array1[::-1])
        array2 = ''.join(array2[::-1])
        
        array3 = (int(array1) + int(array2))
        array3 = str(array3)[::-1]
        cur = dummy = ListNode(array3[0])
        
        for num in array3:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next
