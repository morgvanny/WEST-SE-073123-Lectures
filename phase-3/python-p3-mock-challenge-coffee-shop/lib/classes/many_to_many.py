from statistics import mean


class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if hasattr(self, "name"):
            raise Exception("Name has already been set.")
        elif not isinstance(name, str):
            raise Exception("Name must be a string.")
        elif len(name) < 3:
            raise Exception("Name must be at least 3 characters.")
        else:
            self._name = name
        # if not hasattr(self, "name") and isinstance(name, str) and len(name) > 2:
        #     self._name = name
        # else:
        #     raise Exception("Validation failed.")

    def orders(self):
        return [order for order in Order.all if order.coffee is self]

    def customers(self):
        return list(
            set([order.customer for order in Order.all if order.coffee is self])
        )

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        if self.num_orders() == 0:
            return 0
        else:
            return mean([order.price for order in self.orders()])
            # sum = 0
            # for order in self.orders():
            #     sum += order.price

            # return sum / self.num_orders()

    @classmethod
    def names(cls):
        return [coffee.name for coffee in cls.all]


class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string.")
        elif len(name) not in range(1, 16):
            raise Exception("Name must be between 1 and 15 characters (inclusive).")
        else:
            self._name = name

    def orders(self):
        return [order for order in Order.all if order.customer is self]

    def coffees(self):
        return list(
            set([order.coffee for order in Order.all if order.customer is self])
        )

    def create_order(self, coffee, price):
        return Order(self, coffee, price)

    @classmethod
    def most_aficionado(cls, coffee):
        dict = {}
        max_price = 0.0
        for order in coffee.orders():
            if dict.get(order.customer):
                dict[order.customer] += order.price
            else:
                dict[order.customer] = order.price
            if dict[order.customer] > max_price:
                max_price = dict[order.customer]
                most = order.customer
        if max_price:
            return most

    @classmethod
    def longest_name(cls):
        longest_length = 0
        for c in cls.all:
            if len(c.name) > longest_length:
                longest_length = len(c.name)
                name = c.name
        if longest_length:
            return name

    @classmethod
    def cust_with_longest_name(cls):
        longest_length = 0
        for c in cls.all:
            if len(c.name) > longest_length:
                longest_length = len(c.name)
                customer = c
        if longest_length:
            return customer

    @classmethod
    def ordered_multiple(cls, coffee):
        # dict = {}
        # customers = []
        # for order in coffee.orders():
        #     if dict.get(order.customer):
        #         dict[order.customer] += 1
        #         if dict[order.customer] > 5:
        #             customers.append(order.customer)
        #     else:
        #         dict[order.customer] = 1

        # return customers

        customers = []
        for customer in cls.all:
            num = len(
                [order.coffee for order in customer.orders() if order.coffee is coffee]
            )
            if num > 5:
                customers.append(customer)

        return customers


class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        type(self).all.append(self)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError("Customer must be a customer instance.")
        else:
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if not isinstance(coffee, Coffee):
            raise TypeError("Coffee must be a coffee instance.")
        else:
            self._coffee = coffee

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if hasattr(self, "price"):
            raise Exception("Price has already been set.")
        elif not isinstance(price, float):
            raise TypeError("Price must be a float.")
        elif not (1.0 <= price <= 10.0):
            raise Exception("Price must be between 1.0 and 10.0 (inclusive).")
        else:
            self._price = price
