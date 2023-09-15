from lib.enrollment import Enrollment


class Student:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.__class__.all.append(self)

    def __repr__(self):
        return f"<student Name: {self.full_name}>"

    def enroll_at(self, school):
        Enrollment(school, self)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if isinstance(first_name, str):
            self._first_name = first_name
        else:
            raise Exception("Name must be a string.")

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if isinstance(last_name, str):
            self._last_name = last_name
        else:
            raise Exception("Name must be a string.")

    def enrollments(self):
        return [
            enrollment for enrollment in Enrollment.all if enrollment.student is self
        ]

    def schools(self):
        return [
            enrollment.school
            for enrollment in Enrollment.all
            if enrollment.student is self
        ]
