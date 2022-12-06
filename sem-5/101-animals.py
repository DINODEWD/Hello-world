import random

class MissingParameterError(Exception):
    def __init__(self):
        super().__init__('Missing parameter error: ')

class InvalidParameterError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__('Invalid parameter error: ' + self.message)

class InvalidSoundError(InvalidParameterError):
    def __init__(self):
        super().__init__("sound")

class InvalidAgeError(InvalidParameterError):
    def __init__(self):
        super().__init__("age")

class JungleAnimal:
    def __init__(self, name, age, sound):
        self.name = name
        self.age = age
        self.sound = sound
    def make_sound(self):
        print(self.name + " says " + self.sound + "!")
    def print(self):
        pass
    def daily_task(self):
        pass

class Jaguar(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 15:
            raise InvalidAgeError()
        if self.sound.count("r") < 2:
            raise InvalidSoundError()

    def print(self):
        print(f"Jaguar({self.name}, {self.age}, {self.sound})")

    def daily_task(self, listlistAnimals):
        for i in range(len(listlistAnimals)):
            if type(listlistAnimals[i]) == Lemur or type(listlistAnimals[i]) == Human:
                print(f"{self.name} the Jaguar hunted down {listlistAnimals[i].name} the {type(listlistAnimals[i]).__name__}")
                listlistAnimals.remove(i)
                break

class Lemur(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError()
        if self.sound.count("e") < 1:
            raise InvalidSoundError()
    def print(self):
        print(f"Lemur({self.name}, {self.age}, {self.sound})")
    def daily_task(self, countFruits):
        if countFruits >= 10:
            print(f"{self.name} the Lemur ate a full meal of 10 fruits")
            countFruits -= 10
            return countFruits
        elif countFruits >= 0:
            print(f"{self.name} the Lemur could only find {countFruits} fruits")
            return 0
        else:
            self.make_sound()
            self.make_sound()
            print(f"{self.name} the Lemur couldn't find anything to eat")
            return 0

class Human(JungleAnimal):
    def __init__(self, name, age, sound):
        super().__init__(name, age, sound)
        if self.age > 10:
            raise InvalidAgeError()
        if self.sound.count("e") < 1:
            raise InvalidSoundError()

    def print(self):
        print(f"Human({self.name}, {self.age}, {self.sound})")

    def daily_task(self, listAnimals, listBuildings):
        placeInList = listAnimals.index(self)
        if placeInList == 0:
            if type(listAnimals[1]) == Human:
                listBuildings.append(Building(type = "Insert type: "))
        elif placeInList == (len(listAnimals) - 1):
            if type(listAnimals[(len(listAnimals) - 2)]) == Human:
                listBuildings.append(Building(type = "Insert type: "))
        else:
            if type(listAnimals[placeInList-1]) == Human and type(listAnimals[placeInList+1]):
                listBuildings.append(Building(type = "Insert type: "))

class Building:
    def __init__(self, type):
        self.type = type

fruits = 100
animals = []
buildings = []

names = [
    "Jacob",
    "David",
    "Bobby",
    "Steve",
    "Johanssen",
    "Mac",
    "Jason",
    "Edward",
    "Alex",
    "Maddie",
    "Susan",
    "Abigail",
    "Jessica",
    "Lizzy",
    "Monica",
    "Lorelei",
    "Sandra",
    "Michelle"
]

sounds = [
    "RAAWR",
    "ROAR",
    "Grrr",
    "Shriek",
    "Meow",
    "Eeek",
    "Aaaaa",
    "Speak",
    "I am a Human"
]

for i in range(102):
    num = random.randint(0, 10)

print(f"The jungle now has {len(animals)} animals")

for anim in animals:
    if type(anim) == Lemur:
        fruits = anim.daily_task(countFruits = fruits)
    elif type(anim) == Human:
        anim.daily_task(listAnimals = animals, listBuildings = buildings)
    else:
        anim.daily_task(listAnimals = animals)

print(f"The jungle now has {len(animals)} animals")
print(fruits)
print(animals)
print(buildings)
