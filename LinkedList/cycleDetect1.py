# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        detect = False
        slow = head
        fast = head
        i = 0
        while True:
            
            
            try:
                slow = slow.next
                fast = fast.next.next
            except:
                return False

            
            if slow == fast:
                print("cycle detect")
                return True
                
            if slow.val == None and fast.val == None:
                print("No cycle")
                return False


        
        
