def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("That's not a valid number! Please try again.")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("That's not a valid number! Please try again.")

def run_program(): 
    shopping_cart = {}
    run_program = '0'
    while run_program != '4':
        run_program = input('Welcome to Mike\'s shopping cart app. What would you like to do?\n Remember when entering a price or a quantity use the \"0.00\" format!\n\t To add an item type 1\n\t To remove an item type 2\n\t To update an item quantity/price type 3\n\t To exit type 4\n')
        while not run_program.isdigit():
            run_program = input('Please enter a number')

        if run_program == '1':
            name = input('Enter the name of the item you wish to add: ').lower().title()
            price = get_float('Enter the price: ')
            quantity = get_int('Enter the quantity: ')
            shopping_cart[name] = {'price': price, 'quantity': quantity}
            print('I\'ve updated your cart: ')
            for name, info in shopping_cart.items():
                print(f'Item: {name}, Price: {info["price"]}, Quantity: {info["quantity"]}')

        elif run_program == '2':
            name = input('Enter the name of the item to remove: ').lower().title()
            if name in shopping_cart:
                del shopping_cart[name]
                print('I\'ve updated your cart: ')
            for name, info in shopping_cart.items():
                print(f'Item: {name}, Price: {info["price"]}, Quantity: {info["quantity"]}')
            else:
                print('Item not found.')

        elif run_program == '3':
            name = input('Enter the name of the item to update: ').lower().title()
            if name in shopping_cart:
                new_price = get_float('Enter the new price: ')
                new_quantity = get_int('Enter the new quantity: ')
                shopping_cart[name] = {'price': new_price, 'quantity': new_quantity}
                print('I\'ve updated your cart: ')
            for name, info in shopping_cart.items():
                print(f'Item: {name}, Price: {info["price"]}, Quantity: {info["quantity"]}')
            else:
                print('Item not found.')

    print('Thank you for shopping with us! Here is your final cart: ')
    for name, info in shopping_cart.items():
        print(f'Item: {name}, Price: {info["price"]}, Quantity: {info["quantity"]}')

run_program()

# I'm happy with this overall. There is one small minor bug, and that is after an item is deleted it says item not found in the dictionary when it updates the cart initially, but then it goes away after the next action. I'm not sure why that is happening. Probably something to do with an if, elif, or else statement. I'll have to look into that.