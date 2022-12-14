
class BaseAviary:

    def __init__(self, AviaryName, biom):
        self._aviaryName = AviaryName
        self._biom = biom
        self._square = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._foodTank = 0
        self._maxAnimalsInAviary = 0
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
        if(square>0 and square<=50):
            self._square = square
    @property
    def animalsInAviary(self):
        return self._animalsInAviary
    @property
    def maxAnimalsInAviary(self):
        return self._maxAnimalsInAviary
    @maxAnimalsInAviary.setter
    def maxAnimalsInAviary(self, maxAnimalsInAviary):
        if(maxAnimalsInAviary>0 and maxAnimalsInAviary<=5):
            self._maxAnimalsInAviary = maxAnimalsInAviary
    @property
    def animalTypesInAviaryForPrint(self):
        return self._animalTypesInAviaryForPrint
    @property
    def animalNamesInAviaryForPrint(self):
        return self._animalNamesInAviaryForPrint

    def _printWhenAddingError(self, animalType):
        return(f"Животное {animalType.animalType} не было добавлено.\n1.Подходит ли сосед? {self._IsTheNeighborRight(animalType)}\n2.Подходит ли биом? {self._IsAvailableBiom(animalType)} ({self._biom}/{animalType.biom})\n3.Хватает ли площади? {self._IsAvailableSquare(animalType)} ({animalType.lifeSquare}/{self._square})")
    def _IsTheNeighborRight(self, animalType):
        if(self._animalsInAviary[0].isPredator==animalType.isPredator and self._animalsInAviary[0].animalType==animalType.animalType):
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
        if(len(self._animalTypesInAviaryForPrint)>0):
            for Counter in range(0, self._animalsInAviaryInt):
                RemovingMainMemoryPhrase = RemovingMainMemoryPhrase+self._animalTypesInAviaryForPrint[Counter]+RemovingPhrases[1]+self._animalNamesInAviaryForPrint[Counter]
                if(Counter!=self._animalsInAviaryInt-1):
                    RemovingMainMemoryPhrase=RemovingMainMemoryPhrase+RemovingPhrases[2]
                elif (Counter == self._animalsInAviaryInt-1):
                    RemovingMainMemoryPhrase = RemovingMainMemoryPhrase+RemovingPhrases[3]
            print(RemovingMainMemoryPhrase)
        else:
            print(f"Вы удалили последнее животное! Теперь в вольере {self._aviaryName} не осталось животных.")

## ФУНКЦИЯ ДОБАВЛЕНИЯ ЖИВОТНОГО В ВОЛЬЕР
    def AddAnimalToAviary(self, animalType):
        if(len(self._animalsInAviary)==0 and self._IsAvailableSquare(animalType) and self._IsAvailableBiom(animalType)):
            self._animalsInAviary.append(animalType)
            self._animalsInAviaryInt+=1
            self._square-=animalType.lifeSquare
            self._PrintWhenAdded()
        else:
            if(self._IsTheNeighborRight(animalType) and self._IsAvailableSquare(animalType) and self._IsAvailableBiom(animalType)):
                self._animalsInAviary.append(animalType)
                self._animalsInAviaryInt+=1
                self._PrintWhenAdded()
            else:
                print(self._printWhenAddingError(animalType))

## ФУНКЦИЯ УДАЛЕНИЯ ЖИВОТНОГО ИЗ ВОЛЬЕРА
    def RemoveAnimalFromAviary(self, animalType):
        self._animalNamesInAviaryForPrint.remove(animalType.name)
        self._animalTypesInAviaryForPrint.remove(animalType.animalType)
        self._animalsInAviary.remove(animalType)
        self._PrintWhenRemoved()

    def FeedAnimalsInAviary(self, mass=20, foodType="Бананы"):
        for animalType in self._animalsInAviary:
            animalType.GoEat(foodMass=mass, foodType=foodType)
            self._foodTank-=mass

    def AskWhoWannaEat(self):
        for animalType in self._animalsInAviary:
            if (animalType.isWannaEat):
                print(
                    f"{animalType.name} хочет есть(Он съел всего {animalType.alreadyEated}/{animalType.foodPerDay}, он любит {animalType.foodType})")
            else:
                print(f"{animalType.name} не хочет есть(Он съел {animalType.alreadyEated}/{animalType.foodPerDay})")

    def AnimalsDoSound(self):
        for animalType in self._animalsInAviary:
            animalType.DoSound()