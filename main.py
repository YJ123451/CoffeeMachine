import sys
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
# profit = 0.0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
#wallet and coins
quarters = 0
dimes = 0
nickels = 0
pennies = 0
global wallet
wallet = 0.0
#
def calc(choice):
        #espresso
        if choice == "espresso":
            if resources["water"] < 50:
                print("Sorry, not enough water in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            elif resources["coffee"] < 18:
                print("Sorry, not enough coffee in the machine")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)

            else:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                wallet = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
                if wallet < 1.5:
                 print(f"Sorry, that's not enough money. ${round(wallet,2)} refunded.")
                 choice = input("What would you like?(espresso/latte/cappuccino): ")
                 selection(choice)
                 wallet = 0.0
                resources["water"] -= 50
                resources["coffee"] -= 18
                wallet -= 1.5
                print(f"Here's your espresso, enjoy! ☕ \nHere's ${round(wallet,2)} in change.")
                wallet = 0.0
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
        #latte
        if choice == "latte":
            if resources["water"] < 200:
                print("Sorry, not enough water in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            elif resources["milk"] < 150:
                print("Sorry, not enough milk in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            elif resources["coffee"]< 24:
                print("Sorry, not enough coffee in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            else:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                wallet = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
                if wallet < 2.5:
                    print(f"Sorry, that's not enough money. ${round(wallet, 2)} refunded.")
                    choice = input("What would you like?(espresso/latte/cappuccino): ")
                    selection(choice)
                    wallet = 0.0
                resources["water"] -= 200
                resources["milk"] -= 150
                resources["coffee"] -= 24
                wallet -= 2.5
                print(f"Here's your latte, enjoy! ☕ Here's ${round(wallet,2)} in change.")
                wallet = 0.0
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
        #cappuccino
        if choice == "cappuccino":
            if resources["water"] < 250:
                print("Sorry, not enough water in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            elif resources["milk"]< 100:
                print("Sorry, not enough milk in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            elif resources["coffee"] <24:
                print("Sorry, not enough coffee in the machine.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
            else:
                print("Please insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickels = int(input("How many nickels?: "))
                pennies = int(input("How many pennies?: "))
                wallet = (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)
                if wallet < 3.0:
                    print(f"Sorry, that's not enough money. ${round(wallet, 2)} refunded.")
                    choice = input("What would you like?(espresso/latte/cappuccino): ")
                    selection(choice)
                    wallet = 0.0
                resources["water"] -= 250
                resources["milk"] -= 100
                resources["coffee"] -= 24
                wallet -= 3.0
                print(f"Here;s your cappuccino, enjoy! ☕ Here's ${round(wallet,2)} in change.")
                choice = input("What would you like?(espresso/latte/cappuccino): ")
                selection(choice)
                wallet = 0.0



def selection(choice):
   while choice != "off":
    if choice == "report":
        print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g \nMoney: ${wallet}")
        choice  = input("What would you like?(espresso/latte/cappuccino):")
        selection(choice)
    if choice == "off":
       print("Goodbye!")
       return sys.exit(0)
    elif choice == "espresso" or choice == "cappuccino" or choice == "latte":
        calc(choice)
    elif choice != "report":
        print("Sorry, couldn't get that, try again.")
        choice = input("What would you like?(espresso/latte/cappuccino):")
        selection(choice)
    return choice
choice = input("What would you like?(espresso/latte/cappuccino):")
selection(choice)