# attributes/properties

# behaviors/methods


class Polo():
    def __init__(self, color, size, price):
        self.color = color
        self.size = size
        self.price = price
        self.style = style

    def fold(self):
        print(
            f"FOLDING {self.size.upper()} {self.color.uppper()} THE POLO HERE!")


if__name__ == "__main__":

    polo = Polo("Blue", "Large", 99.99)
    print(polo.color, polo.size, polo.price)
    polo.fold()

    polo2 = Polo(color="Yellow", size="Small", price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color="Green", size="sMediumize", price=69.99)
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()
