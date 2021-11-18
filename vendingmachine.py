#2D Array of 3 Values Per Array
machine_names = [["A1" , "Walkers Crisps", 0.50], ["A2" , "Cheetos Crisps", 0.50], ["B1" , "Cadbury's Chocolate", 0.75],
                ["B2" , "Milky Way Chocolate", 0.80], ["C1" , "Popping Candy", 0.40], ["C2" , "Skittles Candy", 0.60],
                ["D1" , "Ham Sandwich", 1.20], ["D2" , "Cheese Sandwich", 1.40], ["E1" , "Bottle of Coke", 0.95], ["E2" , "Bottle of Water", 1.50]]

#Creating a function for printing the array
def get_table():
    print("\n{:<10} {:<20} {:<10}\n".format("CODE", "ITEM", "PRICE"))  # Adds a Row at the Top with 10,20,10 space between
    for value in machine_names: 
        code, item, price = value 
        print("{:<10} {:<20} £ {:<10}".format(code, item, price)) #Reformatting the code and printing it
        
#Function to iterate through and look for User_Choice
def arrayiterate(user_choice):  
    for i in machine_names:
        if i[0] == user_choice:
            return i

def selection():
    get_table()
    start = True
    while start:
        user_choice = input("@:// ").upper()
        array_look = arrayiterate(user_choice) 
        item_name = (array_look[1])
        item_price = (array_look[2])
        print(f"This Item ({item_name}) Costs: £ {item_price}")  
        input_money(item_name, item_price)
        start = False
  
def input_money(item_name, item_price):
    money = True
    while money:
        money_inputted = float(input("Please Enter Change (£ Format): "))
        if money_inputted >= item_price:
            change = money_inputted - item_price
            print("Please Take Your Item: ", item_name)
            print("Please Take Your Change: £ {:.2f}".format(change))
            money = False
        else:
            print("Change Amount is Too Low or Unknown")

selection()
