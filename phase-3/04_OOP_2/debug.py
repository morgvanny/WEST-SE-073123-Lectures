#!/usr/bin/env python3
# 📚 Review With Students:
# Introduction to Object Oriented programming, classes, instances, methods

# Importing the pet class

from lib.cat import Cat
from lib.owner import Owner

cookie = Cat("cookie", 1, "Dachshund", "hyper", True)

marty = Cat("marty", 1, "long-hair", "hyper", True)

maggie = Cat("maggie", 1, "long-hair", "hyper", True)

me = Owner("Morgan")

anthony = Owner("Anthony")

anthony.adopt(cookie)
me.adopt(marty)


import ipdb

ipdb.set_trace()
