class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and {self.age} years old ")


class Dog(Pet):
    def speak(self):
        print("Meow")


class Cat(Pet):
    def speak(self):
        print("Bark")


p = Pet("tim", 19)
p.show()

c = Cat("Bill", 34)
c.show()
c.speak()
d = Dog("Jill", 25)
d.show()
d.speak()
