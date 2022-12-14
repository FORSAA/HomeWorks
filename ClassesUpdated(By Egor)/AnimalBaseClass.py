class BaseAnimal:

    def __init__(self, name="Стёпа"):

        self._animalType = "   "
        self.name = name
        self._age = 0
        self._mass = 0
        self._sound = "   "

        self._lifeSquare = 0

        self._foodType = []
        self._isPredator = False
        self._alreadyEated = 0
        self._isWannaEat = True
        self._foodPerDay = 0

        self._biom = "   "

    @property
    def animalType(self):
        return self._animalType

    @property
    def age(self):
        return self._age

    @property
    def mass(self):
        return self._mass

    @property
    def sound(self):
        return self._sound

    @property
    def lifeSquare(self):
        return self._lifeSquare

    @property
    def foodType(self):
        return self._foodType

    @property
    def alreadyEated(self):
        return self._alreadyEated


    @property
    def biom(self):
        return self._biom

    @property
    def isPredator(self):
        return self._isPredator

    @property
    def foodPerDay(self):
        return self._foodPerDay

    @age.setter
    def age(self, age):
        if(age>0):
            self._age = age

    def DoSound(self):
        print(f"{self.name} сказал: {self._sound}")

    def GoEat(self, foodType="Бананы", foodMass=10):
        counter = 0
        for i in self._foodType:
            if(foodType == i):
                print(f"{self._sound}, я ем {i}")
                self._mass+=foodMass
                self._alreadyEated+=foodMass
            elif(foodType != i and counter<1):
                print(f"{self._sound}, я не ем {foodType}")
            counter = counter + 1

    @property
    def isWannaEat(self):
        if(self._alreadyEated>=self._foodPerDay):
            return(False)
        else:
            return(True)