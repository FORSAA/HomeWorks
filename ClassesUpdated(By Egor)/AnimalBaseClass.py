class BaseAnimal:

    def __init__(self, name="Стёпа"):

        self._animalType = "   "
        self.name = name
        self._age = 0
        self._mass = 0
        self._sound = "   "

        self.__lifeSquare = 10

        self._foodType = []
        self._isPredator = False
        self._alreadyEated = 0
        self._isWannaEat = True

        self.biom = "   "
