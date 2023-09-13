# !/usr/bin/env python3
# Defines the location of the Python interpreter
# See More => https://stackoverflow.com/a/7670338/8655247

import ipdb

# Classes


# 1. ✅ Create a Pet class

# Note: Add 'pass' to the Pet class

# class Pet:
#     pass


# pet_1 = Pet()

# pet_2 = Pet()

# ipdb.set_trace()

# 2. ✅ Instantiate a few Pet instances

# Compare the Pet instances. Are each of them the same object?

# 3. ✅ Demonstrate __init__
class Pet:

    all = []

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed
        self.all.append(self)

    def print_details(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Breed: {self.breed}")

    def name(self):
        return self._name

    def set_name(self, name):
        if (isinstance(name, str)):
            self._name = name
        else:
            print("Pet name must be a string.")

    def age(self):
        return self._age

    def set_age(self, age):
        if (isinstance(age, int)):
            self._age = age
        else:
            raise Exception("Pet age must be a number")

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        approved_breeds = ["Poodle", "Chihuahua", "Australian Shepherd"]
        if (breed in approved_breeds):
            self._breed = breed
        else:
            raise Exception("Pet's breed must be one of the approved breeds.")

    @classmethod
    def oldest(cls):
        # return max(cls.all, key=lambda pet: pet.age)
        oldest_pet = cls.all[0]

        for pet in cls.all:
            if (pet.age > oldest_pet.age):
                oldest_pet = pet

        return oldest_pet

    name = property(name, set_name)
    age = property(age, set_age)


pet_1 = Pet("Martin", 8, "Poodle")

try:
    pet_2 = Pet("Luna", 4, "Chihuahua")

except:
    print("error occurred")

ipdb.set_trace()
# Add arguments to instances

# Use dot notation to access each Pet instance's attributes

# Update attributes with new values

# Instance Methods

# 4. ✅ Create a "print_pet_details" function that will print each Pet instance's
# attributes

# Review the "self" keyword

# Invoke "print_pet_details" on an instance

# Example Terminal Ouput:
# name: Rose
# age: 11
# breed: Domestic Longhair
# temperament: Sweet

# Object Properties => Attributes that are controlled by methods

# Create an Owner class with two instance methods:

# get_name => Retrieve Owner's name

# set_name => Set Owner's name

# Ensure that Owner's name is a String

# If not, issue warning of "Name must be a string"

# Use property() to compile get_name / set_name and invoke them
# whenever we access an Owner instance's name
j
