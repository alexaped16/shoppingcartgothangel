#shopping cart for goth angel 





def primary_page():
   print("Welcome to Goth Angel! Your cart is currently empty. ")
   user_cart = {}
   options = {"add", "remove", "clear", "quit"}
   shopping_active = True
   while shopping_active:
      answer = input("What would you like to do? Add/Remove/Clear/Quit ")
      while answer not in options: 
         answer = input("Sorry, that is not an acceptable answer. Would you like to: Add/Remove/Clear/Quit ")
         if answer == "quit":
            break
         if answer == 'add':
            break

def add_items():
   item_type: input("What kind of jewelry are you looking for - Necklaces, rings, or earings?")
   


