class Node:
    def __init__(self, DATA):
        self.data = DATA
        self.next = None


class MyLinkedList:

    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.len = 0
        
    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.len:
            return(-1)
                  
        if index == 0: 
            return(self.head.data)

        elif index == (self.len):
            return self.tail.data

        else:
            node = self.head #any element other than head or tail to search
            current = 0 # counter for iteration
            while node is not None:
                if current == index:
                    return node.data
                node = node.next
                current += 1
            return -1 # if list is empty
        
        
    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newHead = Node(val)
        if self.head == None:
            self.head = newHead
        else:
            newHead.next = self.head #next val after new head value after newHead is the oldhead
            self.head = newHead #head is now newHead
        self.len += 1
    
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        newTail = Node(val)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = newTail
        self.len += 1


        
    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        
        if index == 0:
            self.addAtHead(val)
            
        elif index == (self.len):
            self.addAtTail(val)

            
        else:
            indexCounter = 0
            newNode = Node(val)
            current = self.head
            #index -= 1
            #while index != indexCounter:
            for i in range(index-1):
                current = current.next
            newNode.next = current.next  #val in tail is pushed
            current.next = newNode #
            self.len += 1
            

            

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0: # if head to delete
            tempNode = self.head.data #keeping temp variable to return that value
            newHead = self.head.next
            self.head = newHead
            self.len -= 1 #because of deletion
            return tempNode #return the deleted node's value

        else:
            node = self.head 
            current = 0
            prev = None # prev is a previous node which will be the new node after deletion
            while current != index and node.next != None: # conds for deletion(anywhere and end)
                prev = node
                node = node.next
                current += 1
            if current == index: #we're at the node
                prev.next = node.next #pointing the prev node to deleted node's next node
                self.len -= 1 #because of deletion