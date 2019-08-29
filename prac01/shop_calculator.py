total = 0
number_of_items = int(input("Please enter the number of items"))
while number_of_items < 0:
    print("Invalid number")
    number_of_items = int(input("Please enter the number of items"))
price = float(input("Please enter the cost: $"))
for i in range(number_of_items - 1):
    price = float(input("Please enter the cost: $"))
    total += price

if total > 100:
    total *= 0.9

print("total price for", number_of_items, "items is: $", total, sep=' ')
