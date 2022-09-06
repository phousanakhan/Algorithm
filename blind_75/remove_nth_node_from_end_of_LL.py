# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        1. Get the length
        2. Calculate preMove & toDelete
        3. set preMove.next = toDelete.next
        '''
        
        #Get the length
        length = 0
        tempHead = head
        while tempHead != None:
            tempHead = tempHead.next
            length += 1
        
        #Get preMove & toDelete
        preMove = None
        toDelete = None
        tempHead1 = head
        target = length - n
        i = 0
        while i != target:
            preMove = tempHead1
            tempHead1 = tempHead1.next
            toDelete = tempHead1
            i += 1
            
        #Set preMove.next = toDelete.next
        if preMove == None: #this means nth node is the first element of the list
            #return list excluding the first element
            return head.next
        else:
            #3->4->5
            #3->5
            preMove.next = toDelete.next
        return head
#Python copy assignments are essentially pointers to the reference (in this case head). So changing slow, also changes head. However since the original head pointer is to its 'head', we can simply return that as desired with the reflected changes from mutating slow. 
