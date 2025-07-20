# concession stand program

menu = {
    "pizza": 3.00,
    "nachos": 4.5,
    "popcorn": 6.00,
    "fries": 2.50,
    "chips": 1.00,
    "pretzel": 3.50,
    "soda": 3.00,
    "lemonade": 4.25
}
cart = []
total = 0

# calcilate the total
# total = []

# for key, value in menu.items():
#     total += value
# print(f"The total item is: {total}")

# for key, value in menu.items():
#     total.append(value)
# print(sum(total))

print("---------------MENU-----------------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

print("-------------------------")

while True:
    food = input("Enter an item (Q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("---------------YOUR ORDER---------------------")
for food in cart:
    total += menu.get(food)

print()
print(f"total is: {total:.2f}")
