'''
`name` (string with no default)
- `price` (integer with default value 10)
- `weight` (integer with default value 20)
- `flammability` (float with default value 0.5)
- `identifier` (integer, automatically genererated as a random (uniform) number
  anywhere from 1000000 to 9999999, includisve)(inclusive).
'''

import random


class Product():
    def __init__(self, name, id= random.randint(1000000, 9999999), price =10, weight=20, flame =.5):
        self.name = name
        self.price = price 
        self.weight = weight
        self.flame = flame
        self.id = id
    

    def stealability(self):
        self.steal = (self.price / self.weight)
        if (self.steal < .5):
            print("Not so stealable...")
        elif (self.steal < 1):
            print("Kinda stealable.")
        else:
            print("Very stealable!")

    def explode(self):
        self.explode = (self.flame * self.weight)
        if (self.explode < 10):
            print("...fizzle.")
        elif (self.explode < 50):
            print("...boom!")
        else:
            print("...BABOOM!!")


class BoxingGlove(Product):
    def __init__(self, name, id=random.randint(1000000, 9999999), price =10, weight=10, flame =.5):
        super().__init__(name, id, price, weight, flame)
    def explode(self):
        print("...it's a glove.")

    def punch(self):
        if (self.weight < 5):
            print("That tickles.")
        elif (15 > self.weight):
            print("Hey that hurt!")
        else:
            print("OUCH!")
