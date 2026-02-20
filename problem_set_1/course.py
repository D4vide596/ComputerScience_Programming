class Course:
    def __init__(self, name, ects):
        self.name = ""
        self.ects = 0
        self.grades = []

        try:
            if isinstance(name, str):
                self.name = name
            else:
                raise TypeError("The name must be a string")


            if ects>=0 and isinstance(ects, int):
                self.ects = ects
            else:
                raise ValueError("The ects must be a positive integer")

        except (TypeError, ValueError) as e:
            if isinstance(e, TypeError):
                print(f"TypeError: {e}")
            if isinstance(e,ValueError):
                print(f"ValueError: {e}")

    def add_grade(self, value):
        try:
            if isinstance(value, float) or isinstance(value, int):
                value = float(value)
            else:
                raise TypeError("The grade must be a float or an int")

            if 1 <= value <= 6:
                self.grades.append(value)
            else:
                raise ValueError("The grade must be between 1 and 6")

        except (TypeError, ValueError) as e:
            if isinstance(e, TypeError):
                print(f"TypeError: {e}")
            if isinstance(e,ValueError):
                print(f"ValueError: {e}")

    def average(self):
        try:
            sum_grade = 0
            for grade in self.grades:
                sum_grade += grade
            if len(self.grades) != 0:
                return round(sum_grade/len(self.grades), 2)
            else:
                raise ZeroDivisionError("The lists contains zero grades")
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
            return 0

    def is_passed(self):
        return True if self.average() >= 4 else False

    def __str__(self):
        return f"{self.name}, {self.ects}, {self.grades}, {self.average()}, {'Passed' if self.is_passed() else 'Not Passed'}"

    def __repr__(self):
        return self.__str__()