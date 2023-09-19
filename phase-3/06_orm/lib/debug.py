#!/usr/bin/env python3

import ipdb
from pet import Pet

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()
Pet.drop_table()
Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")

# spot.save()
spot = Pet.create("spot", "dog", "chihuahua", "feisty")
martin = Pet.create("martin", "dog", "poodle", "sleepy")

# another = Pet.create("martin", "dog", "poodle", "sleepy")
# one_more = Pet.create("martin", "dog", "poodle", "sleepy")

ipdb.set_trace()
