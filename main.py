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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



print("Hey, thirsty. Want a drink?")

def vending_machine():
    money = 0
    order = input("Order espresso, latte, or cappuccino: ").lower()
    if order == "report":
        print(f'Water: {resources["water"]}mL')
        print(f'Milk: {resources["milk"]}mL')
        print(f'Coffee: {resources["coffee"]}mL')
        print(f'Money: ${money}')

    for drink in MENU:
        if order == drink:
            if resources["water"] < MENU[drink]["ingredients"]["water"]:
                print("Not enough water for this transaction.")
                return vending_machine()
            if resources["milk"] < MENU[drink]["ingredients"]["milk"]:
                print("Not enough milk for this transaction.")
                return vending_machine()
            if resources["coffee"] < MENU[drink]["ingredients"]["coffee"]:
                print("Not enough coffee for this transaction.")
                return vending_machine()
            print(f'Price will be ${MENU[drink]["cost"]}')
            while money < MENU[drink]["cost"]:
                quarters = int(input("Insert any quarters you have: "))
                money += quarters * 0.25
                if money >= MENU[drink]["cost"]:
                    break
                dimes = int(input("Insert any dimes you have: "))
                money += dimes * 0.1
                if money >= MENU[drink]["cost"]:
                    break
                nickels = int(input("Insert any nickels you have: "))
                money += nickels * 0.05
                if money >= MENU[drink]["cost"]:
                    break
                pennies = int(input("Insert any pennies you have: "))
                money += pennies * 0.01
                if money < MENU[drink]["cost"]:
                    print("Insufficient funds. Money refunded.")
                    vending_machine()
            resources["water"] -= MENU[drink]["ingredients"]["water"]
            resources["milk"] -= MENU[drink]["ingredients"]["milk"]
            resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]
            change = money - MENU[drink]["cost"]
            print(f'Here is your {drink}. Enjoy! (Change dispensed: {change})')
            vending_machine()


vending_machine()
