VendingMachine = {
    "030": {'name': 'Chips', 'price': 1.50, 'stock': 10},
    "031": {'name': 'Chocolate', 'price': 2.00, 'stock': 10},
    "032": {'name': 'Cheese Ball', 'price': 1.50, 'stock': 10},
    "033": {'name': 'Nuts', 'price': 1.00, 'stock': 10},
    "034": {'name': 'Donuts', 'price': 3.00, 'stock': 10},
    "040": {'name': 'Cola', 'price': 1.25, 'stock': 15},
    "041": {'name': 'Lemonade', 'price': 1.75, 'stock': 12},
    "042": {'name': 'Iced Tea', 'price': 1.50, 'stock': 20},
    "043": {'name': 'Orange Juice', 'price': 2.00, 'stock': 8},
    "044": {'name': 'Water', 'price': 1.00, 'stock': 25}
}

def userinput():  #allows the user select an item by entering its code from the dictionary
    global VendingMachine
    global choose
    choose = input("Please enter the code to get the items: ")
    if choose in VendingMachine:
        item = VendingMachine[choose]
        print(" ")
        print(f'Code: {choose}, Name: {item["name"]}, price: ${item["price"]}')
        print(" ")
    else:
        print("Invalid code, please try again later")

def moneyinput():  #handles all payment for the selected item in the vending machine
    global VendingMachine
    global choose
    item = VendingMachine[choose]
    price = item['price']
    money = float(input("Please enter the amount of money: "))
    print(f'The amount of money inserted: ${money:.2f}')
    if money >= price:
        change = money - price
        print(f'Please collect your change: ${change:.2f}')
        item['stock'] -= 1  #decrements stock by 1 after a successful transaction
        print(f'Item Dispensed: {item["name"]}')  #message to show item is dispensed
    elif money < price:
        print("Invalid Amount")


def main():  #runs the vending machine system excecuting all other functions as well
    print("Welcome to the VendingMachine")
    print(" ")
    print("Items")
    for code, item in VendingMachine.items():  #display all items with details
        print(f'Code: {code}, Name:{item["name"]}, price:${item["price"]}, Stock:{item["stock"]}')
    print(" ")
    userinput()  #calls the userinput function 
    moneyinput()  #calls the moneyinput function to process transaction
    print(" ")
    for code, item in VendingMachine.items():  #prints updated stock after the sucessful payment
        print(f'Code: {code}, Name:{item["name"]}, price:${item["price"]}, Stock:{item["stock"]}')
    print(" ")

main()
