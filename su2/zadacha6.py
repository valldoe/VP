proceed = True
sum_positive_nums:float = 0
product_positive_nums:float = 1

while proceed:

    inputed = int(input())
    if inputed == -99:
        proceed = False
        break

    if inputed > 0:
        sum_positive_nums += inputed
        product_positive_nums *= inputed

print("sum: " + str(sum_positive_nums))
print("product: " + str(product_positive_nums))