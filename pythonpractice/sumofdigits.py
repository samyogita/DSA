'''
def sumofDigits(num):
    if num == 0:
        return 0
    else:
        return int(num % 10) + sumofDigits(int(num // 10))


print(sumofDigits(11111))
'''
'''
def power(base, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        return base * power(base, exp - 1)


print(power(5, 3))
'''

'''
def gcd(a, b):
    assert int(a) == a and int(b) == b, 'Number must be integer only!'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
print(gcd(48, -18))

'''

def dtob(n):
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * dtob(int(n/2))
print(dtob(13))