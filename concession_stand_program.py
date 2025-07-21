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
discount_items = {"popcorn", "soda"}  # buy 2 get 1 free
cart = []
total = 0.0

# display the menu
print("---------------MENU-----------------")
for key, value in menu.items():
    print(f"{key.title():10}: ${value:.2f}")

print("-------------------------")

# user input loop
while True:
    food = input("\nEnter an item (Q to quit): ").lower()
    if food == "q":
        break
    elif food in menu:
        cart.append(food)
        print(f"✅ {food.title()} added to your cart.")
    else:
        print("Item not on the menu, try again.")

# order summary
print("\n---------------YOUR ORDER---------------------")
if cart:
    order_summary = Counter(cart)

    for item, qty in order_summary.items():
        # price_per_item = qty * menu[item]
        price_per_item = menu[item]

        # apply "buy 2 get 1 free" discount
        if item in discount_items:
            free_items = qty // 3
            charge_qty = qty - free_items
            print(
                f"{item.title():10} x {qty:<3} (includes {free_items} free) @ ${price_per_item:.2f}")
        else:
            charge_qty = qty
            print(f"{item.title():10} x {qty:<3} @ {price_per_item:.2f}")

        item_total = charge_qty * price_per_item
        total += item_total

    print(f"🧾 Total: ${total:.2f}")

    # simulate payment
    while True:
        try:
            payment = float(input("\n💳 Enter payment amount: $"))
            if payment < total:
                print("❌ Not enough! Please enter at least the total amount.")
            else:
                change = payment - total
                print(f"✅ Payment accepted. Your change is: ${change:.2f}")
                print("Thank you for your order!")
                break
        except ValueError:
            print("❌ Invalid input, please enter a valid amount.")

else:
    print("🛒 Your cart is empty")
