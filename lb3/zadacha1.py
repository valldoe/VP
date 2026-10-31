num = int(input())

in_order_digits_list = []

for digit in str(num):
    in_order_digits_list.append(int(digit)) 

in_order_digits_tuple = (in_order_digits_list)
reversed_digits_tuple = (in_order_digits_list[::-1])

print(in_order_digits_tuple)
print(reversed_digits_tuple)