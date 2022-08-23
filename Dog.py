class Dog:
    """un simplu model de dog"""

    def __init__(self, name, age, weight):
        """nume, an si greutate"""
        self.name = name
        self.age = age
        self.weight = weight

    def sit(self):
        """cainele sta"""
        print(f"{self.name} sta")

    def roll_over(self):
        print(f"{self.name} se rostogoleste")

    def bark(self):
        if self.weight > 10:
            print("WOOF")
        else :
            print("woof")

my_dog = Dog("Azor",6,15)
my_dog.bark()
print(f"My dog s name is {my_dog.name}")
my_dog.roll_over()
my_dog.sit()