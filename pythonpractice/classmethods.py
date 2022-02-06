class Person:
    num = 0

    def __init__(self, name):
        self.name = name
        Person.add()

    @classmethod
    def nums(cls):
        return cls.num

    @classmethod
    def add(cls):
        cls.num += 1


p1 = Person("tim")
p2 = Person("jill")
print(Person.nums())