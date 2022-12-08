
class BaseAviary:

    def __init__(self, name, canСontainPredator=False):
        self._aviaryName = name
        self._aviaryBiom = "   "
        self._aviarySquare = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._maxAnimalsInAviary = 0
        self._canContainPredator = canСontainPredator

        self._foodTank = 0

        self._availableBioms = ["Саванна", "Арктика"]

#Getters
    @property
    def printAvailableBioms(self):
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
        AnimalTypesForPrint = []
        AnimalNamesForPrint = []
        Phrases = [f'Отлично, теперь в вольере {self._aviaryName} живут(-ёт): ', ' по имени ', ', ']
        MainMemeoryPhrase = Phrases[0]
        if(self._canContainPredator == False):
            if(self._canContainPredator == False and animalType.isPredator == False and animalType.lifeSquare<=self._aviarySquare):
                if(self._animalsInAviaryInt<=self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                    for i in self._animalsInAviary:
                        AnimalTypesForPrint.append(i.animalType)
                        AnimalNamesForPrint.append(i.name)

                    for a in range(0, self._animalsInAviaryInt):
                        MainMemeoryPhrase=MainMemeoryPhrase+AnimalTypesForPrint[a]+Phrases[1]+AnimalNamesForPrint[a]
                        if(a!=self._animalsInAviaryInt-1):
                            MainMemeoryPhrase=MainMemeoryPhrase+Phrases[2]
                    print(MainMemeoryPhrase)
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к травоядным")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")
#Хищники
        else:
            if (self._canContainPredator == True and animalType.isPredator == True and self._animalsInAviary[0].animalType==animalType.animalType and animalType.lifeSquare <= self._aviarySquare):
                if (self._animalsInAviaryInt <= self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                    for i in self._animalsInAviary:
                        AnimalTypesForPrint.append(i.animalType)
                        AnimalNamesForPrint.append(i.name)

                    for a in range(0, self._animalsInAviaryInt):
                        MainMemeoryPhrase=MainMemeoryPhrase+AnimalTypesForPrint[a]+Phrases[1]+AnimalNamesForPrint[a]
                        if(a!=self._animalsInAviaryInt-1):
                            MainMemeoryPhrase=MainMemeoryPhrase+Phrases[2]
                    print(MainMemeoryPhrase)
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к хищникам")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")


    def RemoveAnimalFromAviary(self, removeableAnimalType):
        counter = 0
        RemovingAnimalTypesForPrint = []
        RemovingAnimalNamesForPrint = []
        RemovingPhrases = [f'Отлично, теперь в вольере {self._aviaryName} остались(-ся): ', ' по имени ', ', ']
        RemovingMainMemoryPhrase = RemovingPhrases[0]
        SearchableName = removeableAnimalType.name
        for i in self._animalsInAviary:
            RemovingAnimalTypesForPrint.append(i.animalType)
            RemovingAnimalNamesForPrint.append(i.name)

        RemovingAnimalNamesForPrint.remove(removeableAnimalType.name)
        RemovingAnimalTypesForPrint.remove(removeableAnimalType.animalType)

        self._animalsInAviaryInt-=1
        for a in range(0, self._animalsInAviaryInt):
            RemovingMainMemoryPhrase = RemovingMainMemoryPhrase + RemovingAnimalTypesForPrint[a] + RemovingPhrases[1] + RemovingAnimalNamesForPrint[a]
            if(a!=self._animalsInAviaryInt-1):
                RemovingMainMemoryPhrase=RemovingMainMemoryPhrase+RemovingPhrases[2]
        print(RemovingMainMemoryPhrase)

    def FeedAnimalsInAviary(self, mass):
        for i in range(0, len(self._animalsInAviary)+1):
            self._animalsInAviary[i].GoEat(foodMass=mass)
            self._foodTank-=mass
    @property
    def AnimalsDoSound(self):
        for i in self._animalsInAviary:
            print(f"{i.name} сказал: {i.sound}")

    @property
    def AskWhoWannaEat(self):
        for i in self._animalsInAviary:
            if(i.isWannaEat):
                print(f"{i.name} хочет есть(Он съел всего {i.alreadyEated}/{i.foodPerDay}, он любит {i.foodType})")
            else:
                print(f"{i.name} не хочет есть(Он съел {i.alreadyEated}/{i.foodPerDay})")