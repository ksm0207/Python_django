class Dog:
    def __init__(self):
        print("woof woof")

    def pee(self):
        print("I Will Pee")


class Puppy(Dog):
    def pee(self):
        print("Go to the Park")
        super().pee()


# pug = Dog()
p = Puppy()
p.pee()
