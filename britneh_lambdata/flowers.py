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
    print(rose.season, rose.size, rose.species)
    rose.pick()

    daisy = Flower("summer", "2", "daisy")
    print(daisy.season, daisy.size, daisy.species)
    daisy.pick()

    tulip = Flower("spring", "3", "tulip")
    print(tulip.season, tulip.size, tulip.species)
    tulip.pick()
