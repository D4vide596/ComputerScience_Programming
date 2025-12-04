# Assignment 7.1 - Black Friday Wishlist (optional)

# Write a program, that uses a dictionary as a storage structure, to implement a wish list.

# The program must continuously present the user with a menu to allow the user to perform different
# operations.

# The first operation allowed is the insertion of a new item in the wishlist (product name and price).
# If an item with the same name is already present in the wishlist, the program must avoid adding it
# again but should print a warning and go on.

# The second option available must allow the user to print the list of available items.

# The third option should request the maximum budget to the user, and then print the list of affordable
# items.

# The last option allows the user to quit the program.

if __name__ == "__main__":

    b_f_w = {}
    repeating = True
    while repeating:

        #menu
        print("1. Add an item to the wishlist")
        print("2. List items in the wishlist")
        print("3. Insert your budget and print the affordable items")
        print("4. Quit")

        choice = int(input("What operation you want to perform? "))

        #1. Add an item to the wishlist
        #The first operation allowed is the insertion of a new item in the wishlist (product name and price).
        # If an item with the same name is already present in the wishlist, the program must avoid adding it
        # again but should print a warning and go on.

        # What operation you want to perform? 1
        # Insert the product name: Monitor
        # Insert the product price: 199.99
        # New product added to the wishlist!

        # Product already added!

        # choices of adding
        if choice == 1:
            
            # name and price of product
            name_product = input("Insert the product name: ")
            price_product = float(input("Insert the product price: "))

            # is it already in the wishlist?
            if name_product in b_f_w:
                print("Product already added!\n\n")
                continue
            
            # adding the product
            b_f_w[name_product] = price_product


        

            
        #2. List items in the wishlist
        # The second option available must allow the user to print the list of available items.

        # What operation you want to perform? 2
        # List of all the items in store:
        # Monitor : 199.99
        # Keyboard : 99.9

        if choice == 2:
            print("List of all the items in store:")

            for name, price in b_f_w.items():
                print(f"{name} : {price}")



        #3. Insert your budget and print the affordable items
        # The third option should request the maximum budget to
        #  the user, and then print the list of affordable items.

        # What operation you want to perform? 3
        # Enter the maximum price: 120
        # List of affordable items:
        # Keyboard : 99.9
        if choice == 3:
            max_price = float(input("Enter the maximum price: "))
            print("List of affordable items:")