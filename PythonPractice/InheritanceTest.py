class Animal:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_habitat(self):
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")


class Dog(Animal):
    def __init__(self):
        super().__init__("Dog")

    def sound(self):
        print("Bow Bow!")


x = Dog()
x.print_habitat()
x.sound()