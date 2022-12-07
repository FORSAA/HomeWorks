
class BaseAviary:

    def __init__(self, name, canContainPredator=False):
        self._aviaryName = name
        self._aviaryBiom = "   "
        self._aviarySquare = "   "
        self._animalsInAviary = []
        self._maxAnimalsInAviary = 0
        self._canContainPredator = canContainPredator

    """GETTERS"""
    @property
    def aviaryName(self):
        return self._aviaryName

    @property
    def aviaryBiom(self):
        return self._aviaryBiom

    @property
    def aviarySquare(self):
        return self._aviarySquare

    @property
    def animalsInAviary(self):
        return self._animalsInAviary

    @property
    def maxAnimalsInAviary(self):
        return self._maxAnimalsInAviary

    @maxAnimalsInAviary.setter
    def maxAnimalsInAviary(self, maxAnimals):
        if(maxAnimals>=0 and maxAnimals<5):
            self._maxAnimalsInAviary = maxAnimals


    def AddAnimalToAviary(self, animalType):
        if True:
            if(self._canContainPredator == False and animalType.isPredator == False and animalType.liveSquare <= self._aviarySquare and animalType.biom == self._aviaryBiom):
                self._animalsInAviary.append(animalType)
            elif (self._canContainPredator == True and animalType.isPredator == True and animalType.liveSquare <= self._aviarySquare and animalType.biom == self._aviaryBiom):
                self._animalsInAviary.append(animalType)
