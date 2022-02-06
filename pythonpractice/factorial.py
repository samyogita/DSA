'''
def factorial(num):
    assert num >= 0 and int(num) == num , " The number must be positive integer only"
    if num in [0,1]:
        return 1
    else:
        return num * factorial(num - 1)


print(factorial(-1))
'''

def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number can't be negative or non integer"
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(0.5))


