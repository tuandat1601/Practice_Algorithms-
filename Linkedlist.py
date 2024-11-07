class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
    def insertAtIndex(self,data,index):
        if (index == 0):
            self.insertAtBegin(data)
        position = 0
        current_node = self.head
        while (position + 1 != index and current_node is not None):
            position += 1
            current_node = current_node.next
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        current_node = self.head
        while(current_node.next):
            current_node = current_node.next
        current_node.next = new_node

    def updateAtIndex(self,data,index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = data
        else:
            while (position + 1 != index and current_node is not None):
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node = current_node.next
                current_node.data =data
            else:
                    print("Index not present")
    def remove_first_node(self):
        if(self.head == None):
            return

        self.head = self.head.next
    def remove_last_node(self):

        if self.head is None:
            return

        current_node = self.head
        while(current_node != None and current_node.next.next != None):
            current_node = current_node.next

        current_node.next = None

    def remove_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        while (position +1 !=index and current_node is not None):
            position += 1
            current_node = current_node.next
        if current_node != None:
            current_node.next = current_node.next.next
        else:
                print("Index not present")
    def remove_node_data(self,data):
        current_node = self.head
        if current_node.data ==data:
            self.remove_first_node()
        
        while(current_node!=None and current_node.data != data):
            current_node = current_node.next
        if current_node ==None:
            return
        else:
            current_node.next = current_node.next.next
    def showAll(self):
        current_node = self.head
        while(current_node):
            print(current_node.data)
            current_node = current_node.next
    def sizeOfLL(self):
        size = 0
        if(self.head):
            current_node = self.head
            while(current_node):
                size = size+1
                current_node = current_node.next
            return size
        else:
            return 0
llist = LinkedList()

# add nodes to the linked list
llist.insertAtEnd('a')
llist.insertAtEnd('b')

llist.insertAtEnd('d')
llist.insertAtIndex('g',3)
llist.remove_at_index(2)
llist.showAll()

