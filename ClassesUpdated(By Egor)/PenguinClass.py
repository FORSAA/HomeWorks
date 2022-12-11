from AnimalBaseClass import BaseAnimal

class PenguinClass(BaseAnimal):

    def __init__(self, name="Стёпа"):
        super().__init__(name)
        self._animalType = "Пингвин"
        self._age = 4
        self._mass = 70
        self._sound = "Пи-пи-пи"
        self._foodPerDay = 3
        self._isPredator = False

        self._lifeSquare = 15

        self._foodType = ["Рыба", "Мясо"]

        self._biom = "Арктика"

    def GoEat(self, foodType="Рыба", foodMass=10):
        counter = 0
        for i in self._foodType:
            if(foodType == i):
                print(f"{self._sound}, я ем {i}")
                self._mass+=foodMass
                self._alreadyEated+=foodMass
            elif(foodType != i and counter<1):
                print(f"{self._sound}, я не ем {foodType}")
            counter = counter + 1