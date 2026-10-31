nums = [int(n) for n in input().split()]

new_nums_list = []

for num in nums:
    if num not in new_nums_list:
        new_nums_list.append(num)

print(new_nums_list)