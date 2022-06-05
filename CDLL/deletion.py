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

    # Reverse traversal of a CDLL
    def reverseTraversal(self):
        if self.head is None:
            print("There are no elements in the linked list")#  
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                if tempNode == self.head:
                    break
                tempNode = tempNode.prev

    # Search for an element in a CDLL
    def searchCDLL(self, nodeValue):
        if self.head is None:
            print("There is no element in the linked list")
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                if tempNode == self.tail:
                    return "The element does not exist"
                tempNode = tempNode.next
    
    # Deletion of an element in CDLL
    def deleteNode(self, location):
        if self.head is None:
            print("There are no elements in the CDLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current = self.head
                index = 0
                while index < location - 1:
                    current = current.next
                    index += 1
                current.next = current.next.next 
                current.next.prev = current
            print("The node has been successfully deleted")


circularDLL = CircularDoublyLinkedList()
circularDLL.CreateDLL(6)
circularDLL.insertCDLL(0,0)
circularDLL.insertCDLL(1,-1)
circularDLL.insertCDLL(2,0)
print([node.value for node in circularDLL])
#circularDLL.traversalCDLL()
#circularDLL.reverseTraversal()
circularDLL.deleteNode(0)
print([node.value for node in circularDLL])

    


     


