# myList = [1, 2, 3, 4, 5, 6]
# print(myList)
# myList[3] = 33
# print(myList)
''' 1 '''

# myList = [1, 2, 3, 4, 5, 6, 7]
# print(myList)
# myList.insert(0,11)
# print(myList)
# newList = [11, 12, 13, 14]
# myList.append(55)
# print(myList)
# myList.extend(newList)
# print(myList)
# myList.pop(1)
# print(myList)
# del myList[0]
# print(myList)
# myList.remove(5)
# print(myList)
''' 2 '''

''' 3 '''
# myList = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# if 20 in myList:
#     print(myList.index(20))
# else:
#     print("Values doesn't exist in the list")
#
#
# def searchList(list, value):
#     for i in list:
#         if i == value:
#             return list.index(value)
#     return "Value doesn't exist"
#
#
# print(searchList(myList, 50))

''' 4 '''
# a = "spam-spam-spam"
# b = list(a)
# print(b)
# a = "spam-spam-spam"
# b = a.split('-')
# print(b)
# print('-'.join(b))
#
# a = [1,2,3,4,5,6,7,8,9,10]
# a[::2]=10,20,30,40,50
# print(a)

# f1 = ['apple','berry','cherry','papaya']
# f2 = f1
# print(f1)
# print(f2)
# f3 = f1[:]
# print(f3)
#
# f2[0] = "Guava"
# print(f2)
# print(f1)
# f3[1] = 'kiwi'
#
# sum=0
# for i in(f1, f2, f3):
#     if i[0] == "Guava":
#         sum += 1
#     if i[1] == "kiwi":
#         sum += 20
#
# print(sum)

numDays = int(input("Number of days"))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day" + str(i+1) +"'s high temp:"))
    temp.append(nextDay)
    total+= temp[i]

avg = round(total/numDays , 2)
print("Average = " +str(avg))

above = 0
for i in temp:
    if i>avg:
        above+=1
print(str(above)+ "day(s) above average")


