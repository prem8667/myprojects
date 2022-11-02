MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


coffee_machine = True
money = 0

while coffee_machine:
    ask = input("What would you like? (espresso/latte/cappuccino): ").lower()


    def check(money, total):
        if ask != 'report' and total > MENU[ask]['cost']:

            change = round((total - MENU[ask]['cost']), 2)
            money = money + total - change
            print(f"Here is your change ${change}")
            print("Here is your coffee ☕")
            resources['water'] = (resources['water'])-(MENU[ask]['ingredients']['water'])
            resources['milk'] = (resources['milk'])-(MENU[ask]['ingredients']['milk'])
            resources['coffee'] = (resources['coffee'])-(MENU[ask]['ingredients']['coffee'])
        elif ask != 'report' and total < MENU[ask]['cost']:
            print("Not enough coins! Here is your money!")



    def resource_check():
        if (resources['water']) < MENU[ask]['ingredients']['water']:
            print("Sorry there is not enough water")
        elif (resources['milk']) < MENU[ask]['ingredients']['milk']:
            print("Sorry there is not enough milk")
        elif (resources['coffee']) < MENU[ask]['ingredients']['coffee']:
            print("Sorry there is not enough coffee")
        else:
            return True


    if ask != 'report' and ask != 'off' and resource_check():
        total = 0
        print("Please insert Coins")
        quarters = int(input("How many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        total += (quarters * 25 + dimes * 10 + nickels * 5 + pennies)/100
        check(money, total)

    elif ask == 'report':
        print(resources)
        print(f"Money : {money}")
    elif ask == 'off':
        coffee_machine = False





