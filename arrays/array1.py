
from array import *
'''
arr1 = array('i', [1, 2, 3, 4, 5, 6])
arr2 = array('d', [1.3, 1.5, 1.6])
#print(arr1)
#print(arr2)

#arr1.insert(6, 7)
#arr1.insert(0, 7)
#print(arr1)


def traverseArray(array):
    for i in array:
        print(i)


traverseArray(arr1)
'''
'''
arr1 = array('i', [1, 2, 3, 4, 5, 6])


def accessElement(array, index):
    if index >= len(array):
        print("No element in that index")
    else:
        print(array[index])


accessElement(arr1, 10)
'''
'''
arr1 = array('i', [1, 2, 3, 4, 5, 6])


def searchArray(array, value):
    for i in array:
        if i == value:
            return array.index(value)
    return "The element does not exist in this array"


print(searchArray(arr1, 3))
'''
arr1 = array('i', [1, 2, 3, 4, 5, 6])

arr1.remove(1)

print(arr1)
