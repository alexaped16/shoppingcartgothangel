
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
    item_type = input("Would you like to buy a necklace, a ring, or earings. Enter an item: ")
    if item_type in cart:
        repeat_item = input("Item already in shopping cart. Would you like to add it again? Yes or No ")
        if repeat_item == 'yes':
            cart[item_type] = cart[item_type] +1
        elif repeat_item == 'no':
            print("Okay, this item will not be added to your cart")   
    else: 
        print("Good choice. This item has been added to your cart. ")
        cart[item_type] = 1
          

def remove_item(cart):
    item_type = input("Enter the name of the item you'd like to remove: ")
    print("Are you sure you would like to remove this item? Yes or No")
    if item_type in cart:
        del(cart[item_type])


def view_cart(cart): 
    if cart:

        for item in cart:
            print("---Current Shopping Cart----")
            print(item, ":",cart[item])
    else:
        print("Your cart is currently empty")

primary_page()
    
            


    

