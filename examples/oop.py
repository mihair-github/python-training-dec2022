class Person:
    count = 0  # class variable

    def __init__(self, name):
        self.name = name  # instance variable
        print("inside __init__", self, id(self))
        self.increment_count()

    def greet(self, greeting):  # instance method
        print(f"{self.name} says <{greeting.capitalize()}!>")

    @classmethod
    def increment_count(cls):  # class method
        cls.count += 1

    @staticmethod
    def get_info():  # static method
        print("This is a static method!")


if __name__ == '__main__':
    p1 = Person("Ana")
    print(p1, id(p1), p1.name)
    p2 = Person("Matei")
    print(p2, id(p2), p2.name)

    print(p1.count, p2.count, Person.count, p1.count is p2.count)
    print(p1.name is p2.name)

    p1.greet("hi")
    p2.greet("good morning")

    Person.get_info()
    p1.get_info()
