'''
- A doubly linked list is a more complex data structure than a singly linked list, but it offers several advantages.
- The main advantage of a doubly linked list is that it allows for efficient traversal of the list in both directions.

Structure:
None <-> data <-> data <-> None
1. Data
2. A pointer to the next node (next)
3. A pointer to the previous node (prev)

Create an empty Doubly Linked List with the following operations:
1. Append
2. Prepend
3. Insert
4. Search
5. Delete
6. Display
'''
class Node:
    def __init__(self,data):
        '''
        - Make the an instance of the Node.
        - Next is the pointer to the next Node.
        - Prev is the pointer to the Node before the current Node 
        '''
        self.data = data
        self.next = None
        self.prev = None
        
class linkedList:
    def __init__(self):
        self.head = None
    
    def clear(self):#Reset the list.
        self.head = None 
        print("THE LIST IS CLEARED")
        return 
    
        
    def insert(self,data,position=0):
        new_node = Node(data)
        if position == 0:#Check if the Input position is the Head.
            new_node.next = self.head
            if self.head is not None:
                new_node.prev = self.head
            self.head = new_node
            return self.head 
        
        curr = self.head 
        for _ in range(position, -1):
            if curr is None:
                break
            curr = curr.next
        
        new_node.prev = curr
        new_node.next = curr.next
        curr.next = new_node
        
        if curr.next is not None:
            new_node.next.prev = new_node
        return 
        
            
    def search(self,key):
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        if curr and curr.data == key:
            print(f"{key} IS IN THE LIST")
            return
        print(f"{key} IS NOT FOUND IN THE LIST")
       
    def delete(self, key):
        curr = self.head

        while curr and curr.data != key:
            curr = curr.next

        if curr is None:
            print("Not Found")
            return

        # Case 1: deleting head
        if curr == self.head:
            self.head = curr.next
            if self.head:
                self.head.prev = None

        # Case 2: deleting middle or tail
        else:
            curr.prev = curr.next
            if curr.next:
                curr.next = curr.prev

        print(f"{key} is Deleted")

    
    def display(self):
        print("None", end=" <-> ")
        curr = self.head
        while curr:
            print(f"{curr.data}<->",end="")
            curr = curr.next
        print("None")

linklist = linkedList()
linklist.insert(1,position=1)
linklist.insert(3,position=2)
linklist.display()