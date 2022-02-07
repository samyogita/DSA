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
            if node.next == self.head:
                break
            node = node.next
    
    #create CSLL

    def create_csll(self, nodevalue):

