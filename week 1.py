#ADD SOME PRODUCT NAMES

#drinks = ['Coca-Cola', 'Coke Zero', 'Water'] 

sandwiches = ['Tuna', 'Egg', 'Chicken']

main_menu_options = {0: 'No', 1 : 'Yes'}

product_menu = { 0 : 'Go back to main menu', 1 : 'Tuna Sandwich Meal', 2 : 'Egg Sandwich Meal', 3 : 'Chicken Sandwich Meal'}

#sandwiches + drinks

print(main_menu_options)

user_input = int(input('Would you like to buy lunch?: ' ))

if user_input == 0:
    print('Exit')

#PRODUCTS MENU

elif user_input == 1:
    print(product_menu)

meal_choice = int(input('Please choose which meal you would like: ')) 

if meal_choice == 0:
    print(main_menu_options)
    int(input('Would you like to buy lunch?: ' ))
    
    if user_input == 0:
        print('Exit')
        
    elif user_input == 1:
        print(product_menu)


