from acme import Product
import random
from random import randint, sample, uniform
import numpy
from numpy import mean 

def generate_products(num):
    products = []
    for i in range(num):
        first = ['Awesome ', 'Shiny ', 'Impressive ', 'Portable ', 'Improved ']
        last = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', 'Balloon']
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        name = ''.join(random.choices(first) + random.choices(last))
        flame = random.uniform(0, 2.5)
        product = Product(name, id, price, weight, flame)
        products.append(product)
    return products


import numpy
from numpy import mean
def inventory_report(products):
    report = []
    for i in range(30):
        item = [products[i].name, products[i].weight, products[i].price, products[i].flame]
        report.append(item)
        flame2 = products[i].flame
        weight2 = products[i].weight
        price2 = products[i].price
        name2 = len(set(products[i].name))
    return  f"ACME CORPORATION OFFICIAL INVENTORY REPORT Unique values:{name2}, Average Price:{ mean(price2)}, Average Flammability: {mean(flame2)}, Average Weight:{mean(weight2)}, {report}"


if __name__ == '__main__':
    print(inventory_report(generate_products()))
