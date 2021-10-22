machine_contents = {
"Walkers Crisps" : 50, 
"Cheetos Crisps" : 50, 
"Cadbury's Chocolate" : 75, 
"Milky Way Chocolate" : 80, 
"Popping Candy" : 40, 
"Skittles" : 60, 
"Ham Sandwich" : 120, 
"Cheese and Tomato Sandwich" : 140,
"Can of Coke" : 95, 
"Bottle of Water" : 150}

machine_names = {
"A1" : "Walkers Crisps", 
"A2" : "Cheetos Crisps", 
"B1" : "Cadbury's Chocolate", 
"B2" : "Milky Way Chocolate", 
"C1" : "Popping Candy", 
"C2" : "Skittles", 
"D1" : "Ham Sandwich", 
"D2" : "Cheese and Tomato Sandwich",
"E1" : "Can of Coke", 
"E2" : "Bottle of Water"}

def selection():
    print("""
         Welcome to the Vending Machine! \n
         (A1): Walkers Crisps (50p) \n
         (A2): Cheetos Crisps (50p) \n
         (B1): Cadbury's Chocolate (75p) \n
         (B2): Milky Way Chocolate (80p) \n
         (C1): Popping Candy (40p) \n
         (C2): Skittles (60p) \n
         (D1): Ham Sandwich (120p) \n
         (D2): Cheese and Tomato Sandwich (140p) \n
         (E1): Can of Coke (95p) \n
         (E2): Bottle of Water (150p)
         """)

    start = True
    while start:
        user_choice = input("@:// ")
        user_choice = user_choice.upper()
        if user_choice in machine_names:
            item_name = machine_names[user_choice]
            item_price = machine_contents[item_name]
            input_money(item_name, item_price)
            start = False
        else:
            print("Selection Not Found , Please Try Again...")
        
def input_money(item_name, item_price):
    money = True
    while money:
        money_inputted = int(input("Please Enter Change: "))
        if money_inputted >= item_price:
            change = money_inputted - item_price
            print("Please Take Your Item: ", item_name)
            print("Please Take Your Change: ", change)
            break
        else:
            print("Change Amount is Too Low or Unknown")

selection()
