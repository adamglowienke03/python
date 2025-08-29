from data_coffee_machine import MENU, resources

def print_report():
    for resource in resources:
        print(f"{resource}: {resources[resource]}ml")
    print(f"Money: ${resources['money']}")

while True:
    choose_drink = input("What would you like? (espresso/latte/cappuccino): ")
    if choose_drink in MENU:
        drink = MENU[choose_drink]
        print(f"Your {choose_drink} costs ${drink['cost']}. Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.10
        nickels = int(input("How many nickels?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        total_inserted = quarters + dimes + nickels + pennies
        if total_inserted < drink['cost']:
            print("Sorry that's not enough money. Money refunded.")
        else:
            resources['money'] += drink['cost']
            change = round(total_inserted - drink['cost'], 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {choose_drink}. Enjoy!")
            for ingredient in drink['ingredients']:
                resources[ingredient] -= drink['ingredients'][ingredient]
    elif choose_drink == "report":
        print_report()