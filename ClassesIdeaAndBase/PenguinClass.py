class Penguin:

    def __init__(self, name="Стёпа"):

        self.__animalType = "Пингвин"
        self.name = name
        self.__age = 7
        self.__mass = 150
        self.__sound = "Пи-пи"

        self.__lifeSquare = 25

        self.__foodType = ["Рыба"]
        self.__isPredator = True
        self.__alreadyEated = 0
        self.__isWannaEat = True

        self.biom = "Арктика"

    @property
    def alreadyEated(self):
        return self.__alreadyEated

    @property
    def lifeSquare(self):
        return self.__lifeSquare

    @property
    def animalType(self):
        return self.__animalType

    @property
    def sound(self):
        return self.__sound

    @property
    def foodType(self):
        return self.__foodType

    @property
    def isWannaEat(self):
        return self.__isWannaEat

    @property
    def isPredator(self):
        return self.__isPredator

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if (age > 0):
            self.__age = age

    @property
    def mass(self):
        return self.__mass

    @mass.setter
    def mass(self, mass):
        if (mass > 0):
            self.__mass = mass

    def GoEat(self, foodType, foodMass):
        for i in self.__foodType:
            if (foodType == i):
                print(f"{self.__sound}, я ем, {foodType}")
                self.__mass += foodMass
                self.__alreadyEated += foodMass
            else:
                print(f"{self.__sound}, фуу, я не ем {foodType}")

    def GoPlay(self):
        print(f"{self.__sound}, я играю")

    def DoSound(self):
        print(f"{self.__sound}")

    def isWannaEat(self):
        if (self.__alreadyEated >= 5):
            print(f"{self.__sound}, я наелся")