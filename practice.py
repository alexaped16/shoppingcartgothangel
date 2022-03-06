
#global variables



def primary_page():
    shopping_cart = {}
    options = {'1','2','3','4'}
    item_type = {'necklace', 'ring', 'earings', 'a necklace', 'a ring' }    

            #welcome message 
    print("Welcome to Goth Angel! Your cart is currently empty. ")

    user_active = True
    while user_active == True:


        print("""
        Would you like to: 
        ----------------
        1: Add item
        2. Remove item
        3: View cart
        4: Exit 

        """)

        option = input("Please enter the number of the option you'd like to choose: ")
        if option == '4':
            print("Thanks for shopping. Come back soon!")
            user_active = False
            break
        elif option == '1': 
            add_item(shopping_cart)
        elif option == '2':
            remove_item(shopping_cart)
        elif option == '3':
            view_cart(shopping_cart)
        else: 
            print("Invalid request. Please enter a valid number: ")
    
    
def add_item(cart):
    item_type = input("Would you like to buy a necklace, a ring, or earings. Enter an item: ").lower()
    complete_design = {}
    color = input("What color would you like your item to be? Lavendar/Soft Pink/Lime Green/Baby Blue ").lower()
    style = input("What beads would you like to use for your item? Smiley Face/Dice/Angel Wing/Flower ").lower()

    #store color : style in a dictionary
    complete_design [color] = style
  
    for color, style in complete_design.items():
            confirmation = input(f"Please confirm your design: A {color} {item_type} with {style} beads. Type 'yes' to confirm, type 'no' to be brought back to the main menu. ")
            if confirmation == 'yes':
                cart[item_type] = 1
                print(f"Wonderful. A {color} {item_type} with {style} beads has been added to your cart. You will now return back to the main menu. ")


def remove_item(cart):
    item_type = input("Enter the name of the item you'd like to remove: ")
    confirm_removal = input(f"Are you sure you want to remove your {item_type} from your cart? Yes or No ")
    if confirm_removal == 'yes':
        if item_type in cart:
            print(f"Your {item_type} has been removed from your cart. You will now return to the main menu. ")
            del(cart[item_type])
    else: 
        print(f"Okay, your {item_type} will stay in your cart. You will now be brought back to the main menu. ")
            

def view_cart(cart): 
    if cart:

        for item in cart:
            item_cost = 20.00
            print("---Current Shopping Cart----")
            print(item, ":",cart[item])
            print(f"{item} is {item_cost}")
    else:
        print("Your cart is currently empty")

primary_page()
    
            


    

