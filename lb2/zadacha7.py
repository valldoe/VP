operation:str = input()

a:int = int(input())
b:int = int(input())
result:float

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/' and b != 0:
    result = a / b
else:
    print("няма такава операция")


print(result)