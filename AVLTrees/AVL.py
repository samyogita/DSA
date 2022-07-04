import queue_ll as queue

class AVLNode:
    def __init__(self, data):
        self.data = data 
        self.leftChild = None
        self.rightChild = None
        self.height =  1


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                customQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                customQueue.enqueue(root.value.rightChild)

def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print('The value is found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print('The value is found')
        else:
            searchNode(rootNode.rightChild, nodeValue)

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height


def rightRotate(disbalancedNode):
    newRoot = disbalancedNode.leftChild
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))   
    newRoot.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    return newRoot 

def leftRotate(disbalancedNode):
    newRoot = disbalancedNode.rightChild
    disbalancedNode.rightChild = disbalancedNode.leftChild.leftChild
    newRoot.leftChild = disbalancedNode
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))   
    newRoot.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)



newAVL = AVLNode(10)
