# concession stand program
from collections import Counter

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
    print(f"{key.title():10}: ${value:.2f}")

print("-------------------------")

# order input loop
while True:
    food = input("Enter an item (Q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"✅{food.title()} added to your cart.")
    else:
        print("Item not on the menu, try again.")

# order summary
print("\n---------------YOUR ORDER---------------------")
if cart:
    order_summary = Counter(cart)

    for item, qty in order_summary.items():
        item_total = qty * menu[item]
        print(
            f"{item.title():10} X {qty:<3} @ ${menu[item]:.2f} each = ${item_total:.2f}")
        total += item_total

    print(f"🧾 Total: ${total:.2f}")

    # simulate payment
    while True:
        try:
            payment = float(input("\n💳 Enter payment amount: $"))
            if payment < total:
                print("❌Not enough! Please enter at least the total amount.")
            else:
                change = payment - total
                print(f"✅Payment accepted. Your change is: ${change:.2f}")
                print("Thank you for your order!")
                break
        except ValueError:
            print("❌Invalid input, please enter a valid amount.")

else:
    print("🛒 Your cart is empty")
