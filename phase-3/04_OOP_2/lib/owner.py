class Owner:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def adopt(self, pet):
        # check if any owner owns this pet
        # add to self.pets if not
        if not pet.owner:
            pet.owner = self
        else:
            print(f"This pet is already owned by {pet.owner.name}.")

    def cats(self):
        from lib.cat import Cat

        return [cat for cat in Cat.all if cat.owner == self]
