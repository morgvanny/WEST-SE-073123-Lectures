# Sequence Types

# Note: use print() to execute the examples. Comment out examples as needed to keep your Terminal
# output clean.

# Creating Lists
# 1. ✅ Create a list of 10 pet names
pet_names = [
    "Rose",
    "Tom",
    "Meow Meow Beans",
    "Mr.Legumes",
    "Luke",
    "Lea",
    "Princess Grace",
    "Spot",
    "Tom",
    "Mini",
    "Paul",
]

# Reading Information From Lists
# 2. ✅ Return the first pet name
# print(pet_names[0])

# 3. ✅ Return all pet names beginning from the 3rd index
# inclusive
# print(pet_names[2:])

# 4. ✅ Return all pet names before the 3rd index
# last element exclusive
# print(pet_names[0:2])

# 5. ✅ Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[2:6])

# 6. ✅ Find the index of a given element => .index()
# print(pet_names.index("Tom"))

# 7. ✅ Reverse the original list => .reverse()
# print(pet_names)
pet_names.reverse()


# 8. ✅ Return the frequency of a given element => .count()
# print(pet_names.count("Tom"))

# Updating Lists
# 9. ✅ Change the first name to all uppercase letters => .upper()
pet_names[0] = pet_names[0].upper()

# 10. ✅ Append a new name to the list => .append()
# pet_names.append("Tom")
# print(pet_names)

# 11. ✅ Add a new name at a specific index => .insert()
pet_names.insert(2, "Jeff")

# 12. ✅ Add two lists together => +
list1 = [1, 2, 3]
list2 = [4, 5, 6]

list1 + list2

# 13. ✅ Remove the final element from the list => .pop()
# item_removed = pet_names.pop()
# print(pet_names)
# 14. ✅ Remove element by specific index => .pop()
# pet_names.pop(-2)
# print(pet_names)

# 15. ✅ Remove a specific element => .remove()
pet_names.remove("Tom")
# print(pet_names)

# 16. ✅ Remove all pet names from the list => .clear()
# pet_names.clear()
# print(pet_names)

# Tuple
# 📚 Review:
# Mutable, Immutable <=> Changeable, Unchangeable

# 17. ✅ Create a Tuple of 10 pet ages => ()
ages = (1, 3, 4, 3, 3, 5, 8, 2, 10)
# print(ages)
# 18. ✅ Print the first pet age => []
# print(ages[0])

# Testing Mutability
# 19. ✅ Attempt to remove an element with ".pop" (should error)
# ages.pop()

# 20. ✅ Attempt to change the first element (should error) => []
# ages[0] = 15

# Tuple Methods
# 21. ✅ Return the frequency of a given element => .count()
# print(ages.count(3))

# 22. ✅ Return the index of a given element  => .index()
# print(ages.index(3))

# 23. ✅ Create a Range
# Note:  Ranges are primarily used in loops
# print(range(50))

# Sets (Stretch Goal)
# 24. ✅ Create a set of 3 pet foods
pet_fav_food = {"house plants", "fish", "bacon"}

# Dictionaries
# Creating
# 25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
pet_info_rose = {"name": "Rose", "age": 11, "breed": "domestic long"}


# 26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed" => dict(...)
pet_info_spot = dict(name="Spot", age=25, breed="boxer")

# Reading
# 27. ✅ Print the pet attribute of "name" using bracket notation
# print(pet_info_rose['temperament'])
# print(pet_info_spot.get('age'))
# 28. ✅ Print the pet attribute of "age" using ".get"
# print(pet_info_rose.get("age"))
# Note: ".get" is preferred over bracket notation in most cases
# because it will return "None" instead of an error


# Updating
# 29. ✅ Update Rose's age to 12 => []
pet_info_rose["age"] = 12
# print(pet_info_rose)

# 30. ✅ Update Spot's age to 26 => .update({...})
pet_info_spot.update({"age": 26, "name": "spot"})
# print(pet_info_spot)

# Deleting
# 31. ✅ Delete Rose's age using the "del" keyword => []
# del pet_info_rose['age']
# print(pet_info_rose)
# 32. ✅ Delete Spot's age using ".pop"
pet_info_rose.pop("age")
# print(pet_info_rose)

# 33. ✅ Delete the last item for Rose using "popitem()"
pet_info_rose.popitem()
# print(pet_info_rose)

# Loops
pet_info = [
    {
        "name": "Rose",
        "age": 1,
        "breed": "domestic long-haired",
    },
    {
        "name": "Spot",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Meow Meow Beans",
        "age": 2,
        "breed": "domestic long-haired",
    },
]

pet_info_2 = [
    {
        "name": "Rose2",
        "age": 11,
        "breed": "domestic long-haired",
    },
    {
        "name": "Spot2",
        "age": 25,
        "breed": "boxer",
    },
    {
        "name": "Meow Meow Beans2",
        "age": 2,
        "breed": "domestic long-haired",
    },
]

# 34. ✅ Loop through a range of 10 and print every number within the range
# ra = range(10)
# for num in ra:
#     print(num)

# 35. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
# for num in range(50, 60, 2):
#     print(num)

# 36. ✅ Loop through the "pet_info" list and print every dictionary
# for pet in pet_info:
#     print(pet)

# 37. ✅ Create a function that takes a list a parameter
# The function should use a "for" loop to loop through the list and print each item
# Invoke the function and pass it "pet_names" as an argument


def loop(l):
    for pet in l:
        print(pet)


# loop(pet_info)
# loop(pet_info_2)

# 38. ✅ Create a function that takes a list as a parameter
# The function should define a counter and set it to 0
# Create a "while" loop
# The loop will continue as long as the counter is less than the length of the list
# Every loop should increase the count by 1
# Return the counter


def while_demo(l):
    counter = 0
    while counter < len(l):
        counter += 1

    return counter


# print(while_demo([1, 2, 3, 4, 5]))

# 39. ✅ Create a function that updates the age of a given pet
# The function should take a list of "dictionaries", "name" and "age" as parameters
# Create an index variable and set it to 0
# Create a while loop
# The loop will continue so long as the list does not contain a name matching the "name" param
# and the index is less then the length of the list
# Every list will increase the index by 1
# If the dictionary containing a matching name is found, update the item's age with the new age
# Otherwise, return 'Pet not found'


def update_age(list, name, age):
    counter = 0
    while list[counter]["name"] != name and counter < len(list) - 1:
        counter += 1
    if list[counter]["name"] == name:
        list[counter]["age"] = age
        return list[counter]
    else:
        return "Pet not found"


# print(update_age(pet_info, "Meow Meow Beans", 3))

# map like
# 40. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# print([pet['name'].upper() for pet in pet_info])

# find like
# 41. ✅ Use list comprehension to find a pet named spot
# print([pet for pet in pet_info if pet['name'] == 'Spot'])

# filter like
# 42. ✅ Use list comprehension to find all of the pets under 3 years old
l = [pet["name"] for pet in pet_info if pet["age"] < 3]
# print(l)
# 43. ✅ Create a generator expression matching the filter above
gen = (pet["name"] for pet in pet_info if pet["age"] < 3)
print(gen)


for name in gen:
    print(name)
