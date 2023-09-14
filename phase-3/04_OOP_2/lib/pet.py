#!/usr/bin/env python3
# Class Attributes and Methods


class Pet:
    # 4. ✅ Define a class attribute (total_pets) and set it to 0

    # Class Attribute
    # What happens with our instances when we update a class attribute?

    def __init__(self, name, age, breed, temperament):
        self.name = name
        self.age = age
        self.breed = breed
        self.temperament = temperament

    def print_pet_details(self, extra=""):
        print(
            f"""\nname: {self.name}\nage: {self.age}\nbreed: {self.breed}"""
            + f"""\ntemperament: {self.temperament}\n"""
        )

    @classmethod
    def add_to_all(cls, pet):
        cls.all.append(pet)


# ipdb.set_trace()

# 5. ✅. Update the class attribute whenever an instance is initialized

# ipdb.set_trace()

# 6. ✅. Create a class method increase_pets that will increment total_pets

# replace Pet.total_pets += 1 in __init__ with increase_pets()

# Instance Method
# def print_pet_details(self):
#     print(f'''
#         name:{self.name}
#         age:{self.age}
#         breed:{self.breed}
#         temperament:{self.temperament}
#     ''')

# Class Method

# ipdb.set_trace()
