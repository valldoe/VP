lower_limit = int(input())
upper_limit = int(input())

count:int = 0
numbers:list = []
   
for n in range(10):
    numbers.append(int(input()))

for n in numbers:
    if(n >= lower_limit and n <= upper_limit):
        count += 1

print("брой числа в интервала: " + count)