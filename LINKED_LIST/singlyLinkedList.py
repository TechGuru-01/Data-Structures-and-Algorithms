'''
- A Linked List is a data structure that is used for storing a collection of data,
 where each element is a separate object.
- The elements are called the Node.
- The first Node is called a head.
- The last Node Points to null. 
- The elements contains both the Data and the Pointer.
- The Data field contains the value of the element.
- The Pointer field contains the address of the element.

Create an empty Singly Linked List with the following operations:
1. Append
2. Preppend
3. Search
4. Delete
5. Display
'''

class Node:
    '''
    - Make the an instance of the Node.
    - Both the Data field and the Pointer field should be empty.
    '''
    def __init__(self, data):
        self.data = data #The Data field
        self.next = None #The Pointer Field
        
        
class linkedList:
    def __init__(self):
        self.head = None #Set the head to empty

    def append(self,data):
       #Case 1: If the head is null, return the input Node.
        new_node = Node(data)
        if self.head is None:
            self.head = new_node 
            return
        #Case 2: If the Head is already occupied, append at the end. 
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def prepend(self,data):
        #Add a new Head.
        new_node = Node(data)
        new_node.next = self.head#Link the new Node to the Head.
        self.head = new_node#Update the Head.
        
    def search(self,key):
        #Note: Traverse to all the Nodes to find the key 
        curr = self.head#Start at The Head.
        while curr and curr.data != key:
            curr = curr.next
        #Case 1: Check If the Node matches the key
        if curr and curr.data == key: 
            print(f"{key} is in the list.")
            return 
        #Case 2: If not return False
        else: 
            print("Not Found.")
            return 
            
    def delete(self,key):
        #Note: Traverse to all the Nodes to find the key 
        curr = self.head
        while curr and curr.data != key:
            prev = curr #Points to the previous Node
            curr = curr.next 
        #Case 1: Check if the Node exist.
        if curr is None:
            print("Not Found")
            return
        #Case 2: Check if the input Data is the Head.
        if curr == self.head:
            self.head = self.head.next
            print(f"{key} is Deleted")
        #Case 3: skip the Node
        else: 
            '''
            What actually happens here, prev remembers the previous Node
            and if curr matches the key, the current node will be skipped.
            
            From: prev -> curr -> next 
            To: prev ------> next
            '''
            prev.next = curr.next
            print(f"{key} is Deleted")
        return 
            
            
    def display(self):
        #Traverse to the whole list starting from the head.
        curr = self.head
        if curr is None:
            return None 
        while curr is not None:#Display the as long as the list is True.
            print(f"{curr.data} -> ", end="")
            curr = curr.next#Progress every Node
        print("None")
        
linked_list = linkedList()
print("This is my Singly Linked List:")
print(" ")
print("1. Append:")
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(9)
linked_list.append(10)
linked_list.display()
print(" ")
print("2. Prepend")
linked_list.prepend(11)
linked_list.prepend(12)
linked_list.prepend(13)
linked_list.display()
print(" ")
print("3. Search:")
linked_list.search(1)
linked_list.search(2)
linked_list.search(5)
linked_list.search(10)
print(" ")
print("4. Delete:")
linked_list.delete(13)
linked_list.delete(10)
linked_list.delete(4)
linked_list.delete(7)
linked_list.display()