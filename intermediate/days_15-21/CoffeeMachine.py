machine_resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}
menu = {
    'espresso': {
        'ingredients': {
            'water_qnt': 50,
            'coffee_qnt': 18
        },
        'cost': 1.5,
    },
    'latte': {
        'ingredients': {
            'water_qnt': 200,
            'coffee_qnt': 24,
            'milk_qnt': 150
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water_qnt': 250,
            'coffee_qnt': 24,
            'milk_qnt': 100
        },
        'cost': 3.0
    }
}

coins = {
    'penny': 0.01,
    'dime': 0.1,
    'nickel': 0.05,
    'quarter': 0.25
}


def calculate_money():
    return 120


# TODO: 2. check sufficient resources
def check_water(coffee_type):
    if menu[coffee_type]['ingredients']['water_qnt'] <= machine_resources['water']:
        return True
    else:
        print("insufficient water")
        return False


def check_coffee(coffee_type):
    if menu[coffee_type]['ingredients']['coffee_qnt'] <= machine_resources['coffee']:
        return True
    else:
        print('insufficient coffe')
        return False


def check_milk(coffee_type):
    if menu[coffee_type]['ingredients']['milk_qnt'] <= machine_resources['milk']:
        return True
    else:
        print("insufficient milk")
        return False


def reduce_water_qnt(coffee_type):
    machine_resources['water'] = machine_resources['water'] - menu[coffee_type]['ingredients']['water_qnt']


def reduce_coffee_qnt(coffee_type):
    machine_resources['coffee'] = machine_resources['coffee'] - menu[coffee_type]['ingredients']['coffee_qnt']


def reduce_milk_qnt(coffee_type):
    machine_resources['milk'] = machine_resources['milk'] - menu[coffee_type]['ingredients']['milk_qnt']


# TODO: 1. print report - how many resources have left
def print_report():
    return print(f"Water: {machine_resources['water']} ml\n"
                 f"Milk: {machine_resources['milk']} ml\n"
                 f"Coffe: {machine_resources['coffee']} g\n"
                 f"Money: ${calculate_money()}\n")


coffee_machine_status = "on"

while coffee_machine_status == "on":

    choice = input("What would you like? espresso/latte/cappuccino\n")

    if coffee_machine_status == "off":
        break

    if choice == "espresso":
        if check_water('espresso') and check_coffee('espresso'):
            reduce_water_qnt('espresso')
            reduce_coffee_qnt('espresso')
            # print(machine_resources)
        else:
            coffee_machine_status = 'off'
    if choice == "latte":
        if check_water('latte') and check_coffee('latte') and check_milk('latte'):
            reduce_water_qnt('latte')
            reduce_coffee_qnt('latte')
            reduce_milk_qnt('latte')
            # print(machine_resources)
        else:
            coffee_machine_status = 'off'
    if choice == "cappuccino":
        if check_water('cappuccino') and check_coffee('cappuccino') and check_milk('cappuccino'):
            reduce_water_qnt('cappuccino')
            reduce_coffee_qnt('cappuccino')
            reduce_milk_qnt('cappuccino')
            # print(machine_resources)

        else:
            coffee_machine_status = 'off'

    if choice == "report":
        print_report()

    if choice != 'espresso' or choice != 'latte' or choice != 'cappuccino' or choice != 'report':
        print("Invalid input")
        break

# TODO: 3. process coins
# TODO: 4. check transaction successful
# TODO: 5. make the coffee
