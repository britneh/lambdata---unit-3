class Flower():
    def __init__(self, season, size, species):
        self.season = season
        self.size = size
        self.species = species
        #self.style = style

    def pick(self):
        print(
            f"PICKING THE {self.season.upper()} {self.species.upper()} TOMORROW!")


if __name__ == "__main__":

    rose = Flower("Winter", "5", "rose")
    print(polo.color, polo.size, polo.price)
    rose.fold()

    daisy = Flower(color="Yellow", size="Small", price=69.99)
    print(polo2.color, polo2.size, polo2.price)
    polo2.fold()

    polo3 = Polo(color="Green", size="Medium", price=69.99)
    print(polo3.color, polo3.size, polo3.price)
    polo3.fold()
