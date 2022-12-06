from AnimalBaseClass import BaseAnimal

class ElefantClass(BaseAnimal):

    def __init__(self, name="Стёпа"):
        super().__init__(name)
        self._animalType = "Слон"
        self._age = 5
        self._mass = 5000
        self._sound = "Siuuuu"

        self._lifeSquare = 25

        self._foodType = ["Бананы", "Кокосы"]

        self._biom = "Саванна"