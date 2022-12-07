

class BaseAviary:

    def __init__(self):
        self._aviaryName = "   "
        self._aviaryBiom = "   "
        self._aviarySquare = "   "

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


    def AddAnimalToAviary(self, animalType):
        pass