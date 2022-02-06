'''
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()
node1 = Node(1)
node2 = Node(2)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2
singlyLinkedList.tail = node2
'''


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SlinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in Linked List

    def insertSLL(self, value, location):
        newNode = Node(value) #initialize value to the node 
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: #insert element at beginning of singly linked list
                newNode.next = self.head   # newNode's next reference to first node's physical location
                self.head = newNode
            elif location == -1: #insert element at the end of the linked list
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    # traverse through the linked list
    def traverse_sll(self):
        if self.head is None:
            print("The single linked list doesn't exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

singlyLinkedList = SlinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 4)
singlyLinkedList.insertSLL(0, 0)
singlyLinkedList.insertSLL(40, 0)
singlyLinkedList.insertSLL(50, -1)
print([node.value for node in singlyLinkedList])
singlyLinkedList.traverse_sll()