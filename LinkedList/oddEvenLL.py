# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        try:
            finalList = []
            oddList = []
            evenList = []

            index = 1
            while head != None:
                if index % 2 == 0:
                    evenList.append(head.val)
                else:
                    oddList.append(head.val)
                head = head.next
                index += 1
            finalList = oddList + evenList

            dummy = ListNode(finalList[0])
            cur = dummy
            for num in finalList:
                cur.next = ListNode(num)
                cur = cur.next
            return dummy.next
        except:
            return None
