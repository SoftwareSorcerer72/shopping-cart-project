shopping_cart = {}

def run_program(): 
    run_program = '0'
    while run_program != '5':
        run_program = input('What would you like to do?\n\t To add an item type 1\n\t To remove an item type 2\n\t To view all items type 3 \n\t To update an item quantity/price type 4\n\t To exit type 5\n')
        while not run_program.isdigit():
            run_program = input('Please enter a number')

        if run_program == '1':
            name = input('Enter the name of the item you wish to add: ').lower().title()
            price = float(input('Enter the price: '))
            quantity = int(input('Enter the quantity: '))
            shopping_cart[name] = {'price': price, 'quantity': quantity}

        elif run_program == '2':
            name = input('Enter the name of the item to remove: ').lower().title()
            if name in shopping_cart:
                del shopping_cart[name]
            else:
                print('Item not found.')

        elif run_program == '3':
            for name, info in shopping_cart.items():
                print('Name: ', name, ', Price: ', info['price'], ', Quantity: ', info['quantity'])

        elif run_program == '4':
            name = input('Enter the name of the item to update: ').lower().title()
            if name in shopping_cart:
                new_price = float(input('Enter the new price: '))
                new_quantity = int(input('Enter the new quantity: '))
                shopping_cart[name] = {'price': new_price, 'quantity': new_quantity}
            else:
                print('Item not found.')

    print('Exiting Shopping Cart.')

run_program()