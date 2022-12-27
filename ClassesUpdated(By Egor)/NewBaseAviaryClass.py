
class BaseAviary:

    def __init__(self, AviaryName):
        self._aviaryName = AviaryName
        self._biom = ""
        self._square = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._foodTank = 0
        self._foodTankMax = 400
        self._maxAnimalsInAviary = 0
        self._animalTypesInAviaryForPrint = []
        self._animalNamesInAviaryForPrint = []
        print(f"Вольер с именем {AviaryName} был успешно создан.")

    @property
    def animalsInAviaryInt(self):
        return self._animalsInAviaryInt
    @property
    def aviaryName(self):
        return self._aviaryName
    @property
    def foodTank(self):
        return self._foodTank
    @foodTank.setter
    def foodTank(self, foodTank):
        if(foodTank<=self._foodTankMax and foodTank>0):
            self._foodTank = foodTank
    @property
    def foodTankMax(self):
        return self._foodTankMax
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
        else:
            print("Минимум-1м², Максимум-50м²")
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
        else:
            print("Максимум 5 животных!")
    @property
    def animalTypesInAviaryForPrint(self):
        return self._animalTypesInAviaryForPrint
    @property
    def animalNamesInAviaryForPrint(self):
        return self._animalNamesInAviaryForPrint

    def _PrintWhenAddingError(self, animalType):
        return(f"Животное {animalType.animalType} не было добавлено.\n1.Подходит ли сосед? {self._IsTheNeighborRight(animalType)}\n2.Подходит ли биом? {self._IsAvailableBiom(animalType)} ({self._biom}/{animalType.biom})\n3.Хватает ли площади? {self._IsAvailableSquare(animalType)} ({animalType.lifeSquare}/{self._square})\n4.Много ли животных?({self._animalsInAviaryInt}/{self._maxAnimalsInAviary})")
    def _IsTheNeighborRight(self, animalType):
        try:
            if(animalType.isPredator!=self._animalsInAviary[0].isPredator):
                return False
            else:
                return True
        except IndexError:
            return True
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
    @property
    def _IsAvailablePlace(self):
        if(self._animalsInAviaryInt+1<=self._maxAnimalsInAviary):
            # print(f"В вольере {self.aviaryName} место есть")
            return True
        else:
            # print(f"В вольере {self.aviaryName} места нет")
            return False

    def _PrintWhenAdded(self):
        Phrases = [f'Отлично, теперь в вольере {self._aviaryName} живут(-ёт): ', ' по имени ', ', ', '.']
        MainMemeoryPhrase = Phrases[0]
        self._animalNamesInAviaryForPrint = []
        self._animalTypesInAviaryForPrint = []

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
        self._animalNamesInAviaryForPrint = []
        self._animalTypesInAviaryForPrint = []

        for iterator in self._animalsInAviary:
            self._animalTypesInAviaryForPrint.append(iterator.animalType)
            self._animalNamesInAviaryForPrint.append(iterator.name)

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
        if(self._animalsInAviaryInt==0 and self._IsAvailableSquare(animalType) and self._IsAvailableBiom(animalType) and self._IsAvailablePlace):
            self._animalsInAviary.append(animalType)
            self._animalsInAviaryInt+=1
            self._square-=animalType.lifeSquare
            self._PrintWhenAdded()
            return True
        else:
            if(self._IsTheNeighborRight(animalType) and self._IsAvailableSquare(animalType) and self._IsAvailableBiom(animalType) and self._IsAvailablePlace):
                self._animalsInAviary.append(animalType)
                self._animalsInAviaryInt+=1
                self._square -= animalType.lifeSquare
                self._PrintWhenAdded()
                return True
            else:
                print(self._PrintWhenAddingError(animalType))
                return False

## ФУНКЦИЯ УДАЛЕНИЯ ЖИВОТНОГО ИЗ ВОЛЬЕРА
    def _RemovingErrorPrint(self, animalType):
        print(f"Ошибка! Невозможно удалить животное {animalType.animalType}! Объект не найден в вольере!")
    def RemoveAnimalFromAviary(self, animalType):
        try:
            self._animalsInAviary.remove(animalType)
            self._animalsInAviaryInt-=1
            self._square+=animalType.lifeSquare
            self._animalNamesInAviaryForPrint.remove(animalType.name)
            self._animalTypesInAviaryForPrint.remove(animalType.animalType)
            self._PrintWhenRemoved()
            return True
        except ValueError:
            self._RemovingErrorPrint(animalType)
            return False

    def FeedAnimalsInAviary(self, mass=20, foodType="Бананы"):
        for animalType in self._animalsInAviary:
            if(self._foodTank>0):
                animalType.GoEat(foodMass=mass, foodType=foodType)
                self._foodTank-=mass
            else:
                print("Не осталось еды в вольере!")

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