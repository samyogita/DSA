class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customList[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapSize

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1, rootNode.heapSize+1):
            print(rootNode.customList[i])


newBinaryHeap = Heap(5)
print(sizeofHeap(newBinaryHeap))