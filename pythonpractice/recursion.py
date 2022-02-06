'''
 1st example

 def openRussiandoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        print("Doll opening....")
        openRussiandoll(doll-1)
openRussiandoll(5)
'''

'''
def firstMethod():
    secondmethod()
    print("I am the first method")


def secondmethod():
    thirdmethod()
    print(" I am the second method")


def thirdmethod():
    fourthmethod()
    print(" I am the third method")


def fourthmethod():
    print(" I am the fourth method")

firstMethod()
'''
'''
def recursiveMethod(n):
    if n < 1:
        print("n is less than 1")
    else:
        recursiveMethod(n-1)
        print(n)

recursiveMethod(4)
'''
