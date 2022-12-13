
class BaseAviary:

    def __init__(self, AviaryName, biom):
        self._aviaryName = AviaryName
        self._biom = biom
        self._square = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._foodTank = 0
        self._maxAnimalsInAviary = 0
        self._isTheNeighborRight = False
        self._animalTypesInAviaryForPrint = []
        self._animalNamesInAviaryForPrint = []

    @property
    def aviaryName(self):
        return self._aviaryName
    @property
    def biom(self):
        return self._biom
    @property
    def square(self):
        return self._square
    @square.setter
    def square(self, square):
        if(square>0 and square<50):
            self._square = square
    @property
    def animalsInAviary(self):
        return self._animalsInAviary
    @property
    def maxAnimalsInAviary(self):
        return self._maxAnimalsInAviary
    @maxAnimalsInAviary.setter
    def maxAnimalsInAviary(self, maxAnimalsInAviary):
        if(maxAnimalsInAviary>0 and maxAnimalsInAviary<5):
            self._maxAnimalsInAviary = maxAnimalsInAviary
    @property
    def animalTypesInAviaryForPrint(self):
        return self._animalTypesInAviaryForPrint
    @property
    def animalNamesInAviaryForPrint(self):
        return self._animalNamesInAviaryForPrint

    def _IsTheNeighborRight(self, animalType):
        if(self._animalsInAviary[0].isPredator==animalType.isPredator and self._animalsInAviary[0]):
            self._isTheNeighborRight=animalType.isPredator
            return True
        elif(animalType.isPredator==False):
            if(animalType.animalType!=animalType.animalType or animalType.animalType==animalType.animalType):
                return True
        else:
            return False

    def _IsAvailableSquare(self, animalType):
        if(self._square>=animalType.lifeSquare):
            return True
        else:
            return False

    def _IsAvailableBiom(self, animalType):
        if(self._biom==animalType.biom):
            return True
        else:
            return False

    def _PrintWhenAdded(self):
        Phrases = [f'Отлично, теперь в вольере {self._aviaryName} живут(-ёт): ', ' по имени ', ', ', '.']
        MainMemeoryPhrase = Phrases[0]

        for iterator in self._animalsInAviary:
            self._animalTypesInAviaryForPrint.append(iterator.animalType)
            self._animalNamesInAviaryForPrint.append(iterator.name)

        for Counter in range(0, self._animalsInAviaryInt):
            MainMemeoryPhrase=MainMemeoryPhrase+self._animalTypesInAviaryForPrint[Counter]+Phrases[1]+self._animalNamesInAviaryForPrint[Counter]
            if (Counter != self._animalsInAviaryInt - 1):
                MainMemeoryPhrase = MainMemeoryPhrase + Phrases[2]
            elif (Counter == self._animalsInAviaryInt - 1):
                MainMemeoryPhrase = MainMemeoryPhrase + Phrases[3]
        print(MainMemeoryPhrase)

    def _PrintWhenRemoved(self):
        RemovingPhrases = [f'Отлично, теперь в вольере {self._aviaryName} остались(-ся): ', ' по имени ', ', ', '.']
        RemovingMainMemoryPhrase = RemovingPhrases[0]

        self._animalNamesInAviaryForPrint.remove(removeableAnimalType.name)
        self._animalTypesInAviaryForPrint.remove(removeableAnimalType.animalType)

        for Counter in range(0, self._animalsInAviaryInt):
            RemovingMainMemoryPhrase = RemovingMainMemoryPhrase+self._animalTypesInAviaryForPrint[Counter]+RemovingPhrases[1]+self._animalNamesInAviaryForPrint[Counter]
            if(Counter!=self._animalsInAviaryInt-1):
                RemovingMainMemoryPhrase=RemovingMainMemoryPhrase+RemovingPhrases[2]
            elif (Counter == self._animalsInAviaryInt-1):
                RemovingMainMemoryPhrase = RemovingMainMemoryPhrase+RemovingPhrases[3]
        print(RemovingMainMemoryPhrase)

    def AddAnimalToAviary(self, animalType):
        if(len(self._animalsInAviary)==0):
            self._animalsInAviary.append(animalType)
            self._animalsInAviaryInt+=1
            self._PrintWhenAdded()
        else:
            if(self._IsTheNeighborRight(animalType) and self._IsAvailableSquare(animalType) and self._IsAvailableBiom(animalType)):
                self._animalsInAviary.append(animalType)
                self._animalsInAviaryInt+=1
                self._PrintWhenAdded()
            else:
                print(f"Животное не было добавлено.\n1.Подходит ли сосед?{self._IsTheNeighborRight(animalType)},\n2.Подходит ли биом?{self._IsAvailableBiom(animalType)}\n3.Хватает ли площади{self._IsAvailableSquare(animalType)}")


