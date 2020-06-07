from acme import Product
import random
from random import randint, sample, uniform


def generate_products(num_products=30):
    first = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
    last = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Balloon']
    price = random.randint(5, 100)
    weight = random.randint(5, 100)
    name = ''.join(random.choices(first) + random.choices(last))
    flame = 0
    iden = 0
    products = Product(name, price, weight, flame, iden)
    return products


def inventory_report(products):
    name = [generate_products() for i in range(0, 30)]
    return name


if __name__ == '__main__':
    print(inventory_report(generate_products()))
