from statistics import mode


class NationalPark:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise Exception("Name must be a string of 3 or more characters.")
        elif hasattr(self, "name"):
            raise Exception("This park already has a name.")
        else:
            self._name = name

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park is self]

    def visitors(self):
        return list(
            set([trip.visitor for trip in Trip.all if trip.national_park is self])
        )

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all if trip.national_park is self]

        return mode(visitors)
        # dict = {}
        # highest = 0
        # for trip in Trip.all:
        #     if trip.national_park is self:
        #         v = trip.visitor
        #         if dict.get(v):
        #             dict[v] += 1
        #         else:
        #             dict[v] = 1
        #         if dict[v] > highest:
        #             highest = dict[v]
        #             best = v
        # if highest:
        #     return best

        def is_threepeat(self):
            dict = {}
            for trip in Trip.all:
                if trip.national_park is self:
                    v = trip.visitor
                    if dict.get(v):
                        dict[v] += 1
                        if dict[v] > 2:
                            return True
                    else:
                        dict[v] = 1
            return False

        @classmethod
        def threepeats(cls):
            return [park for park in cls.all if park.is_threepeat()]

        @classmethod
        def visited_at_least(cls, num):
            return [park for park in cls.all if park.total_visits() >= num]


class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        type(self).all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @visitor.setter
    def visitor(self, visitor):
        if not isinstance(visitor, Visitor):
            raise Exception("Visitor must be a visitor instance.")
        else:
            self._visitor = visitor

    @property
    def national_park(self):
        return self._national_park

    @national_park.setter
    def national_park(self, national_park):
        if not isinstance(national_park, NationalPark):
            raise Exception("National park must be a national park instance.")
        else:
            self._national_park = national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        if not isinstance(start_date, str):
            raise Exception("Start date must be a string.")
        elif len(start_date) < 7:
            raise Exception("Start date must be 7 or more characters.")
        else:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        if not isinstance(end_date, str):
            raise Exception("End date must be a string.")
        elif len(end_date) < 7:
            raise Exception("End date must be 7 or more characters.")
        else:
            self._end_date = end_date


class Visitor:
    def __init__(self, name):
        self.name = name

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

    def trips(self):
        return [trip for trip in Trip.all if trip.visitor is self]

    def national_parks(self):
        return list(
            set([trip.national_park for trip in Trip.all if trip.visitor is self])
        )

    def total_visits_at_park(self, park):
        return len(
            [trip for trip in Trip.all if trip.visitor is self and trip.park is park]
        )
