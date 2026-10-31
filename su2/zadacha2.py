import sys

num_count = int(input())

num_list = []
sum_even = 0
sum_odd = 0
max_even:float = -sys.maxsize #трябва да е минималната стойност която int може да държи...
min_odd:float = sys.maxsize

for i in range(num_count):

    inputed = int(input())
    num_list.append(inputed)

    if inputed == 0:
        print("input is 0")
    if inputed % 2:
        sum_even += inputed

        if inputed > max_even:
            max_even = inputed

    if not inputed % 2:
        sum_odd += inputed

        if inputed < min_odd:
            min_odd = inputed

print(num_list)
print("sum of the even numbers: " + str(sum_even))
print("sum of the odd numbers: " + str(sum_odd))

print("maximum of the even numbers: " + str(max_even))
print("minimum of the odd numbers: " + str(min_odd))
