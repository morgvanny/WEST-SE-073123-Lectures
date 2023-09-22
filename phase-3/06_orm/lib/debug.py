#!/usr/bin/env python3

import ipdb
from owner import Owner
from pet import Pet

# Owner.create_table()
# frank = Owner("frank", "555-555-5555", "frank@gmail.com", "555 Somewhere St.")
# frank.save()
Pet.drop_table()
Owner.drop_table()

Owner.create_table()
Pet.create_table()
# spot = Pet("spot", "dog", "chihuahua", "feisty")

morgan = Owner.create("Morgan")
jason = Owner.create("Jason")
# spot.save()
lucy = Pet.create("lucy", "dog", "great dane", "lazy", jason.id)
martin = Pet.create("martin", "dog", "poodle", "sleepy", morgan.id)
luna = Pet.create("luna", "dog", "chihuahua", "friendly", morgan.id)


# another = Pet.create("martin", "dog", "poodle", "sleepy")
# one_more = Pet.create("martin", "dog", "poodle", "sleepy")

ipdb.set_trace()
