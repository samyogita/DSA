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

circularDLL = CircularDoublyLinkedList()
circularDLL.CreateDLL(6)

print([node.value for node in circularDLL])


    


     


