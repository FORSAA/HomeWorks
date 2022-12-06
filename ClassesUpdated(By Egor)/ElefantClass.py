from AnimalBaseClass import BaseAnimal

class ElefantClass(BaseAnimal):

    def __init__(self, name="Стёпа"):
        super().__init__(name)
        self._animalType = "Слон"
        self._age = 5