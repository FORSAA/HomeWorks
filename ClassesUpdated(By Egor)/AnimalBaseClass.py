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

    """GETTERS"""

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

    """SETTERS"""
    @age.setter
    def age(self, age):
        if(age>0):
            self._age = age

    @property
    def DoSound(self):
        print(f"{self._sound}")

    def GoEat(self, foodType="Бананы", foodMass=10):
        for i in self._foodType:
            counter = 0
            counter+=1
            if(foodType == i):
                print(f"{self._sound}, я ем {i}")
                self._mass+=foodMass
                self._alreadyEated+=foodMass
            elif(counter<1):
                print(f"{self._sound}, я не ем {foodType}")
            else:
                pass
    @property
    def isWannaEat(self):
        if(self._alreadyEated>=self._foodPerDay):
            return(True)
        else:
            return(False)