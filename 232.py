print("=== Cat Food Price Calculator ===")

cart = []

def show_menu():
    print("\nChoose cat food:")
    print("1. Salmon Cat Food - 160 pesos / kg")
    print("2. Whiskas Wet Cat Food - 69 pesos / sachet")
    print("3. Cutie Cat Sea Food - 120 pesos / kg")
    print("4. Happy Furreal - 67 pesos / kg")
    print("5. Meow Mix - 87 pesos / kg")
    print("6. Feline Sardines - 56 pesos / can")
    print("7. Harringtons Cat Food - 69 pesos / pack")
    print("8. Remove item")
    print("9. Decrease item quantity")
    print("10. Show receipt")
    print("0. Exit")

def get_quantity():
    while True:
        try:
            qty = int(input("Enter quantity: "))
            if qty > 0:
                return qty
            print("Quantity must be at least 1.")
        except:
            print("Invalid input.")

def add_item(name, price):
    qty = get_quantity()
    subtotal = price * qty
    cart.append({"name": name, "price": price, "qty": qty, "subtotal": subtotal})
    print(f"Added: {name} x{qty} = {subtotal} pesos")

def show_receipt():
    print("\n=== Customer Receipt ===")
    if not cart:
        print("No items bought yet.")
        return
    total = 0
    for i, item in enumerate(cart, 1):
        print(f"{i}. {item['name']} x{item['qty']} - {item['subtotal']} pesos")
        total += item['subtotal']
    print("\nTotal price:", total, "pesos")

def remove_item():
    show_receipt()
    if not cart: return
    try:
        idx = int(input("Enter item number to remove: ")) - 1
        if 0 <= idx < len(cart):
            removed = cart.pop(idx)
            print("Removed:", removed['name'])
        else:
            print("Invalid item number.")
    except:
        print("Invalid input.")

def decrease_quantity():
    show_receipt()
    if not cart: return
    try:
        idx = int(input("Enter item number to decrease: ")) - 1
        if 0 <= idx < len(cart):
            item = cart[idx]
            print(f"Current qty of {item['name']}: {item['qty']}")
            dec = int(input("How many to decrease? "))
            if dec >= item['qty']:
                print("Quantity is now zero. Item removed.")
                cart.pop(idx)
            else:
                item['qty'] -= dec
                item['subtotal'] = item['qty'] * item['price']
                print(f"Updated: {item['name']} x{item['qty']} = {item['subtotal']} pesos")
        else:
            print("Invalid item number.")
    except:
        print("Invalid input.")

while True:
    show_menu()
    choice = input("Enter choice: ")

    if choice == "1":
        print("\nSalmon Cat Food:")
        print("a. 1 kilo - 160")
        print("b. 1/2 kilo - 80")
        print("c. 1/4 kilo - 40")
        size = input("Choose size (a/b/c): ")

        if size == "a": add_item("Salmon Cat Food (1 kilo)", 160)
        elif size == "b": add_item("Salmon Cat Food (1/2 kilo)", 80)
        elif size == "c": add_item("Salmon Cat Food (1/4 kilo)", 40)
        else: print("Invalid size.")


    elif choice == "2":
        add_item("Whiskas Wet Cat Food", 69)

    elif choice == "3":
        print("\nCutie Cat Sea Food:")
        print("a. 1 kilo - 120")
        print("b. 1/2 kilo - 60")
        print("c. 1/4 kilo - 30")
        size = input("Choose size (a/b/c): ")

        if size == "a": add_item("Cutie Cat Sea Food (1 kilo)", 120)
        elif size == "b": add_item("Cutie Cat Sea Food (1/2 kilo)", 60)
        elif size == "c": add_item("Cutie Cat Sea Food (1/4 kilo)", 30)
        else: print("Invalid size.")

    elif choice == "4":
        print("\nHappy Furreal:")
        print("a. 1 kilo - 67")
        print("b. 1/2 kilo - 33.5")
        print("c. 1/4 kilo - 16.75")
        size = input("Choose size (a/b/c): ")

        if size == "a": add_item("Happy Furreal (1 kilo)", 67)
        elif size == "b": add_item("Happy Furreal (1/2 kilo)", 33.5)
        elif size == "c": add_item("Happy Furreal (1/4 kilo)", 16.75)
        else: print("Invalid size.")

    elif choice == "5":
        print("\nMeow Mix:")
        print("a. 1 kilo - 87")
        print("b. 1/2 kilo - 43.5")
        print("c. 1/4 kilo - 21.75")
        size = input("Choose size (a/b/c): ")

        if size == "a": add_item("Meow Mix (1 kilo)", 87)
        elif size == "b": add_item("Meow Mix (1/2 kilo)", 43.5)
        elif size == "c": add_item("Meow Mix (1/4 kilo)", 21.75)
        else: print("Invalid size.")

    elif choice == "6":
        add_item("Feline Sardines (can)", 56)

    elif choice == "7":
        add_item("Harringtons Cat Food (pack)", 69)

    elif choice == "8":
        remove_item()

    elif choice == "9":
        decrease_quantity()

    elif choice == "10":
        show_receipt()

    elif choice == "0":
        print("Thank you! Meow 🐱")
        break

    else:
        print("Invalid menu choice.")
