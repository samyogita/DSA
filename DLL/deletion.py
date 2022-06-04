

from platform import node


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Create a doubly linked list 
    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully"

    # Insertion method in doubly linked list 
    def insertNode(self, nodeValue, location):
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode 
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0 
                while index > location - 1:
                    tempNode = tempNode.next 
                    index += 1 
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode

    # Traversal in doubly linked list
    def traverseDLL(self):
        if self.head is None:
            print("There is not any element to traverse")
        else: 
            tempNode = self.head 
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    # Reverse traversal in doubly linked list
    def reverseTraversalDLL(self):
        if self.head is None:
            print("There is not any element in the linked list")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    # Search method in DLL
    def searchDLL(self, nodeValue):
        if self.head is None:
            return "There is no element in the linked list"
        else: 
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "Node does not exist"

    # Deleting a node from the linked list
    def deleteNode(self, location):
        if self.head is None:
            print("There is no element in the linked list")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
               
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                current = self.head
                index = 0
                while index > location - 1:
                    current = current.next
                    index += 1
                current.next = current.next.next
                current.next.prev = current

            print("The node has been successfully deleted")
     
doublyLL = DoublyLinkedList()
doublyLL.createDLL(5)

doublyLL.insertNode(0,0)
doublyLL.insertNode(2,1)

print([node.value for node in doublyLL])
# doublyLL.traverseDLL()
#doublyLL.reverseTraversalDLL()
#print(doublyLL.searchDLL(2))
doublyLL.deleteNode(5)
print([node.value for node in doublyLL])
