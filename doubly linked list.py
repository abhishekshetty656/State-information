class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.previous = temp

    def insert_at_position(self, data, pos):
        if pos <= 0:
            print("Position should be >= 1")
            return
        if pos == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1
        while temp and count < pos - 1:
            temp = temp.next
            count += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        new_node.previous = temp
        if temp.next:
            temp.next.previous = new_node
        temp.next = new_node

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

# Usage
dll = DoublyLinkedList()

dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_end(30)

dll.insert_at_beginning(5)
dll.insert_at_position(15, 3)

print("Forward Traversal:")
dll.display_forward()


        
