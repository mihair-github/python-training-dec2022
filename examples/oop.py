from datetime import date
import random


class Person:
    count = 0  # class variable
    MIN_DATE_OF_BIRTH = date(1940, 1, 1)

    def __init__(self, name: str, date_of_birth: date):
        self.name = name  # instance variable
        self._date_of_birth = date_of_birth
        # print("Current instance (inside init)", self, id(self))
        # print("Current class (inside init):", self.__class__, id(self.__class__))
        self._increment_count()

    @property
    def date_of_birth(self):
        # print("getter called!")
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, value):
        # print(f"setter called with {value}!")
        if value < self.MIN_DATE_OF_BIRTH:
            raise ValueError("Invalid date of birth")
        self._date_of_birth = value

    @date_of_birth.deleter
    def date_of_birth(self):
        # print("deleter called!")
        del self._date_of_birth

    @property
    def age(self):
        diff = date.today() - self.date_of_birth  # timedelta object
        return int(diff.days / 365.25)

    def greet(self, greeting):  # instance method
        print(f"{self.name} says <{greeting.capitalize()}!>")

    @classmethod
    def _increment_count(cls):  # class method
        # print("Current class (inside increment_count):", cls, id(cls))
        cls.count += 1

    @staticmethod
    def get_info():  # static method
        print("This is a static method!")

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth

    def __str__(self):
        return f"Person {self.name} ({self.date_of_birth})"


class Student(Person):
    count = 0

    def __init__(self, name: str, date_of_birth: date, university: str):
        self.university = university
        super().__init__(name, date_of_birth)

    def __str__(self):
        return f"{self.name} ({self.date_of_birth} - {self.university})"

    def get_grade(self, subject):
        return random.randint(1, 10)


if __name__ == '__main__':
    p1 = Person("Ana", date(1999, 12, 3))
    # print("Current class (outside class):", Person, id(Person))
    # print(f"Current instance (outside class): {p1} {id(p1)} {p1.name}")
    p2 = Person("Matei", date(1992, 4, 13))
    # print(p2, id(p2), p2.name)

    print(p1.count, p2.count, Person.count, p1.count is p2.count)
    print(p1.name is p2.name)

    p1.greet("hi")
    p2.greet("good morning")

    Person.get_info()
    p1.get_info()

    print(p1 < p2)

    print(p1.date_of_birth)  # getter for name
    p1.date_of_birth = date(1989, 12, 3)  # setter for name
    print(p1.date_of_birth)  # getter for name

    print(p1.age)

    # del p1.date_of_birth  # deleter for name
    # print(p1.date_of_birth)  # getter for name

    s1 = Student("George", date(2001, 5, 6), "ASE București")
    s1.greet("Hello")
    print(f"{s1.name} is {s1.age} years old and studies at {s1.university}.")

    print("Maths grade:", s1.get_grade("maths"))

    print("Student count:", Student.count)
    print("Person count:", Person.count)
