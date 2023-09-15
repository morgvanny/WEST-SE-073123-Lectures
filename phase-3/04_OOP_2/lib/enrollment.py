class Enrollment:
    all = []

    def __init__(self, school, student):
        self.school = school
        self.student = student
        self.__class__.all.append(self)

    @property
    def school(self):
        return self._school

    @school.setter
    def school(self, school):
        from lib.school import School

        if isinstance(school, School):
            self._school = school
        else:
            raise Exception("School must be set to a school object.")

    @property
    def student(self):
        return self._student

    @student.setter
    def student(self, student):
        from lib.student import Student

        if isinstance(student, Student):
            self._student = student
        else:
            raise Exception("Student must be set to a student object.")
