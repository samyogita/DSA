class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class circular_sll:
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
    
    # Creation of circular singly linked list

    def createCSLL(self, nodevalue):
        node = Node(nodevalue)
        node.next = node
        self.head = node
        self.tail = node 
        return "The CSLL has been created"
    
    # Insertion of a node in circular singly linked list

    def insertCSLL(self, value, location):
        if self.head is None:
            return "The head reference is none"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next 
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next 
                tempnode.next = newNode
                newNode.next = nextnode
            
            return "The node has been successfully inserted "


    # Traversal of a node in circular singly linked list
    def traversalCSLL(self):
        if self.head is None:
            print("There id not any element for traversal")

        else:
            tempNode = self.head
            print("Traversal")
            while tempNode:
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    # Searching for a node in circular singly linked list
    def  searchCSLL(self, nodevalue):
        if self.head is None:
            return "There is not any node in CSLL"
        
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodevalue:
                    return tempNode.value 
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    return "The node does not exist in this CSLL"

    # Delete a node from a circular singly linked list
    def deleteNode(self, location):
        if self.head is None: 
            print("There is not any node in CSLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head 
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next 
                    node.next = self.head
                    self.tail = node
            else:
                tempNode = self.head 
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1 
                nextNode = tempNode.next
                tempNode.next = nextNode.next


circularSLL = circular_sll()
circularSLL.createCSLL(0)

print([node.value for node in circularSLL])

circularSLL.deleteNode(1)
print([node.value for node in circularSLL])



                


        
        


