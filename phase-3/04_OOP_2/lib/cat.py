# 7. ✅. Create a subclass of Pet called Cat
# import Pet from lib.pet
from lib.pet import Pet


class Cat(Pet):
    all = []

    def __init__(self, name, age, breed, temperament, indoor, owner=None):
        super().__init__(name, age, breed, temperament)
        self.indoor = indoor
        self.__class__.all.append(self)
        self.owner = owner

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        from lib.owner import Owner

        if owner is None or isinstance(owner, Owner):
            self._owner = owner

    @classmethod
    def all_cats(cls):
        return [cat for cat in cls.all if isinstance(cat, cls)]


# class Dog(Pet):
#     def __init__(self, name, age, breed, temperament):
#         self.name = name
#         self.age = age
#         self.breed = breed
#         self.temperament = temperament
#         self.__class__.add_to_all(self)


# cookie = Cat("cookie", 1, "Dachshund", "hyper", True)

# dog = Dog("cookie", 1, "Dachshund", "hyper")

# 8. ✅. Create Cat class + __init__ that takes all the parameters from Pet and an
# additional parameter called indoor (Boolean)

# Use super to pass the Pet parameters to the super class

# Add an indoor attribute

# ipdb.set_trace()

# 9. ✅. Create a method unique to the Cat subclass called talk which
# returns the string "Meow!"

# ipdb.set_trace()

# 10. ✅. Create a method called print_pet_details to match the print_pet_details in Pet

# Add super().print_pet_details() and print the indoor attribute
