
class BaseAviary:

    def __init__(self, name, cancontainpredator=False):
        self._aviaryName = name
        self._aviaryBiom = "   "
        self._aviarySquare = 0
        self._animalsInAviary = []
        self._animalsInAviaryInt = 0
        self._maxAnimalsInAviary = 0
        self._canContainPredator = cancontainpredator

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
        if(self._canContainPredator == False):
            if(self._canContainPredator == False and animalType.isPredator == False and animalType.lifeSquare<=self._aviarySquare):
                TypesMemoryForPrint = []
                NamesMemoryForPrint =[]
                counter = 0
                animalList = len(self._animalsInAviary)
                if(self._animalsInAviaryInt<=self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                    for i in self._animalsInAviary:
                        TypesMemoryForPrint.append(i.animalType)
                        NamesMemoryForPrint.append(i.name)
                    for counter in range(0, len(TypesMemoryForPrint)):
                        if(len(self._animalsInAviary)>=2 and counter<=animalList-1):
                            print(f"Отлично, теперь в вольере {self.aviaryName}: {TypesMemoryForPrint[counter]} по имени {NamesMemoryForPrint[counter]} и {TypesMemoryForPrint[counter-1]} по имени {NamesMemoryForPrint[counter-1]}")
                        elif(len(self._animalsInAviary)<2 and animalList<2):
                            print(f"Отлично, теперь в вольере {self.aviaryName}: {TypesMemoryForPrint[counter]} по имени {NamesMemoryForPrint[counter]}")
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к травоядным")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")
#Хищники
        else:
            if (self._canContainPredator == True and animalType.isPredator == True and animalType.lifeSquare <= self._aviarySquare):
                TypesMemoryForPrint = []
                NamesMemoryForPrint = []
                counter = 0
                if (self._animalsInAviaryInt <= self._maxAnimalsInAviary):
                    self._animalsInAviary.append(animalType)
                    self._animalsInAviaryInt+=1
                    for i in self._animalsInAviary:
                        TypesMemoryForPrint.append(i.animalType)
                        NamesMemoryForPrint.append(i.name)
                    for counter in range(0, len(TypesMemoryForPrint)):
                        print(f"Отлично, теперь в вольере {self.aviaryName}:{TypesMemoryForPrint[counter], NamesMemoryForPrint[counter]}")
                else:
                    print(f"Вольер переполнен! {self._animalsInAviaryInt}/{self._maxAnimalsInAviary}")
            else:
                print(f"\nНевозможно добавить {animalType.animalType} в вольер к травоядным")
                print(f"1. Может содержать хищников? {self._canContainPredator}, Ваше животное хищник? {animalType.isPredator}.\n2. Размеры вольера? {self._aviarySquare}, Нужно животному? {animalType.lifeSquare}")


    def RemoveAnimalFromAviary(self, removeableAnimalType):
        counter = 0
        TypesMemoryForPrint = []
        NamesMemoryForPrint = []
        for removeableAnimalType in self._animalsInAviary:
            if(removeableAnimalType == self._animalsInAviary[counter]):
                try:
                    self._animalsInAviary.remove(removeableAnimalType)
                    print(f"\nТеперь в вольере {self.aviaryName} остались(-ся): {self._animalsInAviary[counter].animalType} по имени {self._animalsInAviary[counter].name}")
                except ValueError:
                    print("Животное не найдено!")
            counter+=1

    def FeedAnimalsInAviary(self, mass):
        for i in range(0, len(self._animalsInAviary)+1):
            self._animalsInAviary[i].GoEat(foodMass=mass)
            self._foodTank-=mass

    def AnimalsDoSound(self):
        for i in self._animalsInAviary:
            i.DoSound