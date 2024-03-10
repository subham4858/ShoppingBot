shopping_cart = {}

prices = {
    "t-shirt": 15,
    "jeans": 30,
    "shoes": 50,
    "hat": 10
}

print("Welcome to the Shopping Bot!")
print("Available items:")
for item, price in prices.items():
    print(f"{item}: ${price}")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'quit':
        print("Goodbye!")
        break

    elif user_input.lower() == 'cart':
        if not shopping_cart:
            print("Your shopping cart is empty.")
        else:
            print("Your shopping cart:")
            for item, quantity in shopping_cart.items():
                print(f"{item}: {quantity}")

    elif user_input.lower() == 'checkout':
        total = sum(prices[item] * quantity for item, quantity in shopping_cart.items())
        print(f"Total: ${total}")
        confirmation = input("Would you like to proceed with the purchase? (yes/no): ")
        if confirmation.lower() == 'yes':
            print("Thank you for your purchase!")
            shopping_cart.clear()
        else:
            print("Purchase canceled.")

    elif user_input.lower() in prices:
        item = user_input  
        quantity = int(input("Enter quantity: "))
        if item in shopping_cart:
            shopping_cart[item] += quantity
        else:
            shopping_cart[item] = quantity

    else:
        print("Sorry, I didn't understand that.")