from lib.enrollment import Enrollment


class School:
    all = []

    def __init__(self, name):
        self.name = name
        self.__class__.all.append(self)

    def __repr__(self):
        return f"<school Name: {self.name}>"

    def enroll(self, student):
        Enrollment(self, student)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 2:
            self._name = name
        else:
            raise Exception("Name must be a string that has at least 3 characters.")

    def enrollments(self):
        return [
            enrollment for enrollment in Enrollment.all if enrollment.school is self
        ]

    def students(self):
        return [
            enrollment.student
            for enrollment in Enrollment.all
            if enrollment.school is self
        ]

    def unenroll(self, student):
        Enrollment.all = [
            enrollment
            for enrollment in Enrollment.all
            if not (enrollment.school is self and enrollment.student is student)
        ]
