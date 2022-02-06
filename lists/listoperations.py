shoppingList = ["Milk", "Cheese", "Butter"]
print(shoppingList[-1])
print('Milk' in shoppingList)
for i in shoppingList:
    print(i)
for i in range(0,3):
    shoppingList[i] = shoppingList[i] + "+"
    print(shoppingList[i])

empty = []
for i in empty:
    print("I am empty")