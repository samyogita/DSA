# Day 1 - 11, 15, 10, 6
# Day 2 - 10, 14, 11, 5
# Day 3 - 12, 17, 12, 8
# Day 4 - 15, 18, 14, 9

import numpy as np
twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9]])
#print(twoDArray)

# newTwoDArray = np.insert(twoDArray, 1, [[1, 2, 3, 4]], axis=1)
# print(newTwoDArray)

'''
def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print('Incorrect index')
    else:
        print(array[rowIndex][colIndex])


accessElements(twoDArray, 2, 3)
'''
'''
def traverse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverse(twoDArray)
'''

'''
def search(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
               return 'The values is located at index ' + str(i) + " " + str(j)
    return 'Element not found'


print(search(twoDArray, 14))
'''

newTDArrayy = np.delete(twoDArray, 0, axis=0)
print(newTDArrayy)



