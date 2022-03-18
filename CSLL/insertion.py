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

circularSLL = circular_sll()
print(circularSLL.createCSLL(1))
circularSLL.insertCSLL(0, 0)
circularSLL.insertCSLL(2, -1)
circularSLL.insertCSLL(3, -1)
circularSLL.insertCSLL(2, 2)
print([node.value for node in circularSLL])


                


        
        


