#!/usr/bin/python3

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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_enough(order_ingredient):

    """checks to see if there is enough ingredient left in resources"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def calculate_money():
    """returns total of the coins entered"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total


def successful_transaction(money_recieved, drink_cost):
    """returns True if transaction is successful or false is money is insfficient"""
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is ${change} in change")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct drink ingredient from resource ingredient"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}🍵")


on = True
while on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_enough(drink["ingredients"]):
            payment = calculate_money()
            if successful_transaction(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])

