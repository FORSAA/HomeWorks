from NewBaseAviaryClass import *

class BaseZooClass(BaseAviary):

    def __init__(self, name):
        self._aviaryList = []
        self._zooName = name
        self._zooSquare = 0
        self._aviaryNames = []
        self._aviaryAnimals = []
        self._aviaryCountInt = 0


    @property
    def aviaryList(self):
        return self._aviaryList
    @property
    def zooName(self):
        return self._zooName
    @property
    def zooSquare(self):
        return self._zooSquare
    @zooSquare.setter
    def zooSquare(self, zooSquare):
        if(zooSquare<100 and zooSquare>0):
            self._zooSquare = zooSquare

    def _WhenAddedPrint(self, aviary):
        Phrases = [f"Ура! Теперь в зоопарке {self._zooName} есть вольеры: ", ',', '.']
        MainPrintPhrase = Phrases[0]

        if (len(self._aviaryList) > 0):
            for i in self._aviaryList:
                self._aviaryNames.append(aviary.aviaryName)

        for Counter in range(0, self._aviaryCountInt):
            MainPrintPhrase=MainPrintPhrase+self._aviaryNames[Counter]
            if(Counter!=self._aviaryCountInt-1):
                MainPrintPhrase=MainPrintPhrase+Phrases[1]
            elif(Counter==self._aviaryCountInt-1):
                MainPrintPhrase=MainPrintPhrase+Phrases[2]
        print(MainPrintPhrase)

    def _IsEnoughPlace(self, aviary):
        if(self._zooSquare<=aviary.square):
            return True
        else:
            return False

    def AddAviaryToZoo(self, aviary):
        if(self._IsEnoughPlace(aviary)):
            self._aviaryList.append(aviary)
            self._aviaryCountInt+=1
            self._zooSquare-=aviary.square
            self._WhenAddedPrint(aviary)
        else:
            print(f"Не удалось добавить вольер в зоопарк {self._zooName}! Не хватает места для вольера!({self._zooSquare}m²/{aviary.square}m²)")

    def _TransferSucceflyPrint(self, animalType, aviary1From, aviary2To):
        print(f"Перемещение успешно! {animalType.animalType} {animalType.name} перемещен из вольера {aviary1From.aviaryName} в вольер {aviary2To.aviaryName}!")
    def _TransferErrorPrint(self, animalType, aviary1From, aviary2To):
        print(f"Перемещение не удалось! {animalType.animalType} {animalType.name} не перемещен из вольера {aviary1From.aviaryName} в вольер {aviary2To.aviaryName}!")
    def _CheckAnimalInAviaryBeforeRemove(self, animalType, aviaryForCheck):
        for i in aviaryForCheck._animalsInAviary:
            if(i==animalType):
                return True
            else:
                return False


    def TransferAnimalBetweenAviaries(self, animalType, aviary1From, aviary2To):
        TestVar1 = 0
        TestVar2 = 0
        for i in self._aviaryList:
            if(i==aviary1From):
                TestVar1 = i.maxAnimalsInAviary
            elif(i==aviary2To):
                TestVar2 = i.maxAnimalsInAviary

        if(self._CheckAnimalInAviaryBeforeRemove(animalType, aviary1From) and aviary2To._IsAvailablePlace and aviary2To._IsAvailableBiom(animalType) and aviary2To._IsAvailableSquare(animalType) and aviary2To._IsTheNeighborRight(animalType)):
            self._TransferSucceflyPrint(animalType, aviary1From, aviary2To)
            print("\n")
            aviary1From.RemoveAnimalFromAviary(animalType)
            print("\n")
            aviary2To.AddAnimalToAviary(animalType)
        else:
            self._TransferErrorPrint(animalType, aviary1From, aviary2To)

    def AskWhoNeedFoodForAviaries(self):
        counter = 0
        for i in self._aviaryList:
            if(i.foodTank<i.foodTankMax/2):
                print(f"Вольер {i.aviaryName} нуждается в еде!")
                counter+=1
        if(counter==0):
            print("Вольерам не нужна еда.")
