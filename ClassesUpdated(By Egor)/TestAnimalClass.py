import unittest
from TigerClass import TigerClass
from ElefantClass import ElefantClass
from PenguinClass import PenguinClass

class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.Penguin = PenguinClass("Пингвин")
        self.Elefant = ElefantClass("Слон")
        self.Tiger = TigerClass("Тигр")
        self.animals = [self.Penguin, self.Elefant, self.Tiger]

    def testIsWannaEat(self):
        animalAlreadyEatedList = []
        animalIsWannaEatList = []
        for i in self.animals:
            i.GoEat(foodMass=50)
            animalAlreadyEatedList.append(i.alreadyEated)
            animalIsWannaEatList.append(i.isWannaEat)

        AlreadyEatedActual = (animalAlreadyEatedList[0], animalAlreadyEatedList[1], animalAlreadyEatedList[2])
        AlreadyEatedExpected = (50, 50, 50)

        IsWannaEatActual = (animalIsWannaEatList[0], animalIsWannaEatList[1], animalIsWannaEatList[2])
        IsWannaEatExpected = (False, False, False)

        self.assertEqual(AlreadyEatedExpected, AlreadyEatedActual)
        self.assertEqual(IsWannaEatExpected, IsWannaEatActual)
