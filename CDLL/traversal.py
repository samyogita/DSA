from platform import node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None
    
    
    
class CircularDoublyLinkedList:    
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head 
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    # Creation of a circular doubly linked list
    def CreateDLL(self, nodeValue):
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "New CDLL has been created successfully"
    
    # Insertion of a circular doubly linked list
    def insertCDLL(self, value, location):
        if self.head is None:
            return "There are no elements in the linked list"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode 
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode 
            else:
                tempNode = self.head
                index = 0 
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
            return "Node has been created successfully created"

    # Traversing through a CDLL
    def traversalCDLL(self):
        if self.head is None:
            print("The CDLL does not exist")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                if tempNode == self.tail:
                    break
                else:
                    tempNode = tempNode.next


circularDLL = CircularDoublyLinkedList()
circularDLL.CreateDLL(6)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,-1)
circularDLL.insertCDLL(2,2)
print([node.value for node in circularDLL])
circularDLL.traversalCDLL()


    


     


