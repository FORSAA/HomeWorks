
class BaseAviary:

    def __init__(self, name, canContainPredator=False):
        self._aviaryName = name
        self._aviaryBiom = "   "
        self._aviarySquare = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._maxAnimalsInAviary = 0
        self._canContainPredator = canContainPredator

        self._foodTank = 0

        self._availableBioms = ["Саванна", "Арктика"]

        self._animalTypesInAviaryForPrint = []
        self._animalNamesInAviaryForPrint = []


#Getters
    @property
    def PrintAvailableBioms(self):
        print("\nДоступные биомы вольера:")
        for i in self._availableBioms:
            print(f"{i}")
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

#Травоядные
    def AddAnimalToAviary(self, animalType):
        Phrases = [f'Отлично, теперь в вольере {self._aviaryName} живут(-ёт): ', ' по имени ', ', ']
        MainMemeoryPhrase = Phrases[0]
        if(self._canContainPredator == False):
            if(self._canContainPredator == False and animalType.isPredator == False and animalType.lifeSquare <= self._aviarySquare):
                if(self._animalsInAviaryInt<=self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1

                    for iterator in self._animalsInAviary:
                        self._animalTypesInAviaryForPrint.append(iterator.animalType)
                        self._animalNamesInAviaryForPrint.append(iterator.name)

                    for Counter in range(0, self._animalsInAviaryInt):
                        MainMemeoryPhrase=MainMemeoryPhrase+self._animalTypesInAviaryForPrint[Counter]+Phrases[1]+self._animalNamesInAviaryForPrint[Counter]
                        if(Counter!=self._animalsInAviaryInt-1):
                            MainMemeoryPhrase=MainMemeoryPhrase+Phrases[2]
                    print(MainMemeoryPhrase)
                else:
                    print(f"Вольер {self._aviaryName} переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к травоядным")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")
#Хищники
        else:
            if (self._canContainPredator == True and animalType.isPredator == True and animalType.lifeSquare <= self._aviarySquare):
                if (self._animalsInAviaryInt <= self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                    for iterator in self._animalsInAviary:
                        self._animalTypesInAviaryForPrint.append(iterator.animalType)
                        self._animalNamesInAviaryForPrint.append(iterator.name)

                    for Counter in range(0, self._animalsInAviaryInt):
                        MainMemeoryPhrase=MainMemeoryPhrase+self._animalTypesInAviaryForPrint[Counter]+Phrases[1]+self._animalNamesInAviaryForPrint[Counter]
                        if(Counter!=self._animalsInAviaryInt-1):
                            MainMemeoryPhrase=MainMemeoryPhrase+Phrases[2]
                    print(MainMemeoryPhrase)
                else:
                    print(f"Вольер {self._aviaryName} переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")

            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к хищникам")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")


    def RemoveAnimalFromAviary(self, removeableAnimalType):
        RemovingPhrases = [f'Отлично, теперь в вольере {self._aviaryName} остались(-ся): ', ' по имени ', ', ']
        RemovingMainMemoryPhrase = RemovingPhrases[0]

        self._animalNamesInAviaryForPrint.remove(removeableAnimalType.name)
        self._animalTypesInAviaryForPrint.remove(removeableAnimalType.animalType)

        self._animalsInAviaryInt-=1
        for Counter in range(0, self._animalsInAviaryInt):
            RemovingMainMemoryPhrase = RemovingMainMemoryPhrase+self._animalTypesInAviaryForPrint[Counter]+RemovingPhrases[1]+self._animalNamesInAviaryForPrint[Counter]
            if(Counter!=self._animalsInAviaryInt-1):
                RemovingMainMemoryPhrase=RemovingMainMemoryPhrase+RemovingPhrases[2]
        print(RemovingMainMemoryPhrase)

    def FeedAnimalsInAviary(self, mass=20):
        for i in self._animalsInAviary:
            i.GoEat(foodMass=mass)
            self._foodTank-=mass

    def AnimalsDoSound(self):
        for i in self._animalsInAviary:
            print(f"{i.name} сказал: {i.sound}")


    @property
    def AskWhoWannaEat(self):
        for iterator in self._animalsInAviary:
            if(iterator.isWannaEat):
                print(f"{iterator.name} хочет есть(Он съел всего {iterator.alreadyEated}/{iterator.foodPerDay}, он любит {iterator.foodType})")
            else:
                print(f"{iterator.name} не хочет есть(Он съел {iterator.alreadyEated}/{iterator.foodPerDay})")
