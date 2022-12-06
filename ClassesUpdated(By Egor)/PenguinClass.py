from AnimalBaseClass import BaseAnimal

class PenguinClass(BaseAnimal):

    def __init__(self, name="Стёпа"):
        super().__init__(name)
        self._animalType = "Пингвин"
        self._age = 4
        self._mass = 70
        self._sound = "Пи-пи-пи"

        self._lifeSquare = 15

        self._foodType = ["Рыба", "Мясо"]

        self._biom = "Арктика"