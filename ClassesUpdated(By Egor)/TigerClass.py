from AnimalBaseClass import BaseAnimal

class TigerClass(BaseAnimal):

    def __init__(self, name="Стёпа"):
        super().__init__(name)
        self._animalType = "Тигр"
        self._age = 7
        self._mass = 150
        self._sound = "Ррр-р-р"
        self._foodPerDay = 20
        self._isPredator = True

        self._lifeSquare = 25

        self._foodType = ["Мясо"]

        self._biom = "Саванна"

    def GoEat(self, foodType="Мясо", foodMass=10):
        counter = 0
        for i in self._foodType:
            if(foodType == i):
                print(f"{self._sound}, я ем {i}")
                self._mass+=foodMass
                self._alreadyEated+=foodMass
            elif(foodType != i and counter<1):
                print(f"{self._sound}, я не ем {foodType}")
            counter = counter + 1