
from textwrap import indent


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
    

    #insertion into a singly linked list

    def insertSLL(self, value, location):
        newnode = Node(value)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
        else:
            if location == 0:
                newnode.next = self.head 
                self.head = newnode
            elif location == -1:
                newnode.next = None
                self.tail.next = newnode
                self.tail = newnode
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = newnode
                newnode.next = nextnode
                if tempnode == self.tail:
                    self.tail = newnode
    
    # traversal of a SLL
    def traverse_sll(self):
        if self.head is None:
            print("Linked list doesnot exist")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    
    #searching for a given element in a given list

    def search_sll(self, nodevalue):
        if self.head is None:
            return "List doesnot exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodevalue:
                   return node.value
                node = node.next
            return "The value doesnot exist in the list"
    
    def delete_node(self, location):
        if self.head is None:
            print("The Linked list doesnot exist")
        else:
            if location == 0:
                if self.head == self.tail: #only one element
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail: #only one element
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail: #self.tail stores physical location of last node
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location - 1: #traverse till the node which is before the node we want to delete
                    tempnode = tempnode.next
                    index += 1
                nextnode = tempnode.next
                tempnode.next = nextnode.next

    #delete entire sll
    def del_entire_sll(self):
        if self.head is None:
            print("The linked list doesnot exist")
        else:
            self.head = None
            self.tail = None





singlyLinkedList = SlinkedList()
singlyLinkedList.insertSLL(1, 1)
singlyLinkedList.insertSLL(2, 1)
singlyLinkedList.insertSLL(3, 1)
singlyLinkedList.insertSLL(4, 1)
singlyLinkedList.insertSLL(0, 4)
singlyLinkedList.insertSLL(0, 0)


print([node.value for node in singlyLinkedList])
singlyLinkedList.delete_node(1)
singlyLinkedList.del_entire_sll()
print([node.value for node in singlyLinkedList])

