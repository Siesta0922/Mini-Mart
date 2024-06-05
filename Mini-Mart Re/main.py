from Data import Beverage, Snacks, Sanitary_Items, Cleaning_Items, art, Product
print(art)

class ShoppingCart:
    def __init__ (initialize):
        initialize.items = []

    def add_item(initialize, product, quantity):   # Append means Add to List
        initialize.items.append({'Product': product, 'Quantity': quantity}) # Parameter are inside the key Product and Quantity

    def calculate_total(initialize):    # Perform Calculations
        total = sum(item['Product'].price * item['Quantity'] for item in initialize.items)
        return total
    
    def apply_vat(initialize):
        vat_rate = 0.12
        vat_amount = initialize.calculate_total() - (initialize.calculate_total() / (1+vat_rate))
        return vat_amount
    
    def display_cart(initialize):
        print("Your Shopping Cart:")
        total = initialize.calculate_total()
        vat = initialize.apply_vat()
        for item in initialize.items:
            product = item['Product']
            quantity = item['Quantity']
            print(f"Quantity: {quantity} ; {product.name} Php {(product.price * quantity):,.2f}")
        print(f"Initital Total: Php {total - vat:,.2f}")
        print(f"Value Added Tax: Php {vat:,.2f}")
        print(f"Total (including VAT): Php {total:,.2f}")

    def remove_item(initialize, product):
        for item in initialize.items:
            if item['Product'] == product:
                initialize.items.remove(item)
                print(f"{product.name} removed from cart.")
                return
        print(f"{product.name} not found in cart.")

def display_category_products(category, product_list): #Display the items with Price
    print(f"\nAvailable {category}:")
    for i, product in enumerate(product_list): #Enumerate = list them {I + 1 because enumerate will start with zero} 
        print(f"{i + 1}. {product.name} - Php {product.price:,.2f}")

def main():
    cart = ShoppingCart()

    while True:
        print("\nCategories:")
        print("1. Beverages")
        print("2. Chips")
        print("3. Cleaning Items")
        print("4. Sanitary Items")
        print("5. Show Cart")
        print("r. To Reduce or Remove Item")
        print("q. Quit")

        choice = input("Enter your choice: ")
        choice.lower()

        if choice == '1':
            display_category_products("Beverages", Beverage) # displaying beverages and accessing the database beverages
        elif choice == '2':
            display_category_products("Chips", Snacks) # displaying chips and accessing the database chips
        elif choice == '3':
            display_category_products("Cleaning Items", Cleaning_Items) # displaying cleaning items and accessing the database cleaning items
        elif choice == '4':
            display_category_products("Sanitary Items", Sanitary_Items) # displaying Sanitary items and accessing the database Sanitary items
        elif choice == '5':
            cart.display_cart()
        elif choice == 'r':
            print()
            cart.display_cart()
            product_index = int(input("Enter the product number to reduce quantity: ")) - 1
            if 0 <= product_index < len(cart.items):
                selected_item = cart.items[product_index]
                selected_product = selected_item['Product']
                quantity_to_reduce = int(input(f"Enter the quantity to reduce (1-{selected_item['Quantity']}): "))
                if 1 <= quantity_to_reduce <= selected_item['Quantity']:
                    selected_item['Quantity'] -= quantity_to_reduce
                    if selected_item['Quantity'] == 0:
                        cart.remove_item(selected_product)
                    print(f"{selected_product.name} quantity reduced.")
                else:
                    print("Invalid quantity. Please try again.")
            else:
                print("Invalid product number. Please try again.")
        elif choice == 'q': #End Program
            break
        else:
            print("Invalid choice. Please try again.")

        if choice in ['1', '2', '3', '4']:
            category_choice = input("Enter the product number to add to cart (Press B to go back) ").lower()
            if category_choice == 'b':
                continue
            elif category_choice.isdigit():
                category_choice = int(category_choice)
                if choice == '1' and 1 <= category_choice <= len(Beverage):
                    selected_product = Beverage[category_choice - 1]
                elif choice == '2' and 1 <= category_choice <= len(Snacks):
                    selected_product = Snacks[category_choice - 1]
                elif choice == '3' and 1 <= category_choice <= len(Cleaning_Items):
                    selected_product = Cleaning_Items[category_choice - 1]
                elif choice == '4' and 1 <= category_choice <= len(Sanitary_Items): 
                    selected_product = Sanitary_Items[category_choice - 1]
                else:
                    print("You have inputted an invalid input, Try Again") #Invalid input = return to home page
                    continue
                quantity = int(input("Enter the quantity: "))
                cart.add_item(selected_product, quantity)
                print(f"{selected_product.name} added to cart.")
            else:
                print("Invalid choice. Please try again.")
main()