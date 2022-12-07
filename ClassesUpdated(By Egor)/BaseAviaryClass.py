
class BaseAviary:

    def __init__(self, name, cancontainpredator=False):
        self._aviaryName = name
        self._aviaryBiom = "   "
        self._aviarySquare = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._maxAnimalsInAviary = 0
        self._canContainPredator = cancontainpredator

#Getters
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

    @aviarySquare.setter
    def aviarySquare(self, aviarySquare):
        if(aviarySquare>0 and aviarySquare<=50):
            self._aviarySquare = aviarySquare

    @maxAnimalsInAviary.setter
    def maxAnimalsInAviary(self, maxAnimalsInAviary):
        if(maxAnimalsInAviary<=5 and maxAnimalsInAviary>0):
            self._maxAnimalsInAviary = maxAnimalsInAviary

    def AddAnimalToAviary(self, animalType):
        if(self._canContainPredator == False):
            if(self._canContainPredator == False and animalType.isPredator == False and animalType.lifeSquare<=self._aviarySquare):
                if(self._animalsInAviaryInt<=self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к травоядным")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")

        if(self._canContainPredator):
            if (self._canContainPredator == True and animalType.isPredator == True and animalType.lifeSquare <= self._aviarySquare and animalType.biom == self._aviaryBiom):
                if(self._animalsInAviaryInt<=self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к хищникам")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")
