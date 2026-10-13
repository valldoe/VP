from sympy import isprime

num:int = int(input())

if num <= 0:
    print("въведете число, различно от нула")
    exit

if isprime(num):
    print("числото е просто")
else:
    print("числото не е просто")