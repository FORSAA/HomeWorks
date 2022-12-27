import unittest
from SavannaAviaryClass import SavannaAviary
from ArcticAviaryClass import ArcticAviary
from TigerClass import TigerClass
from ElefantClass import ElefantClass
from PenguinClass import PenguinClass

class AviaryTest(unittest.TestCase):

    def setUp(self):
        self.SavannaAviary = SavannaAviary("Вольер-Саванна")
        self.ArcticAviary = ArcticAviary("Вольер-Арктика")
        self.SavannaAviary.square = 50
        self.ArcticAviary.square = 50
        self.SavannaAviary.maxAnimalsInAviary = 5
        self.ArcticAviary.maxAnimalsInAviary = 5
        self.SavannaAviary.foodTank = 400
        self.ArcticAviary.foodTank = 400
        self.Tiger = TigerClass("Даня")
        self.Tiger2 = TigerClass("Кирилл")
        self.Penguin = PenguinClass("Илья")
        self.Elefant = ElefantClass("Валера")

    def AddAnimalToAviary(self, animalType):
        return self.SavannaAviary.AddAnimalToAviary(animalType)


    def testAddAnimalToAviary(self):
        Expected = True
        Actual = self.SavannaAviary.AddAnimalToAviary(self.Tiger)
        self.assertEqual(Expected, Actual)

    def testSecondAddAnimalToAviary(self):
        self.testAddAnimalToAviary()
        Expected = True
        Actual = self.SavannaAviary.AddAnimalToAviary(self.Tiger2)
        self.assertEqual(Expected, Actual)

    def testRemoveAnimalFromAviary(self):
        self.testSecondAddAnimalToAviary()
        Expected = True
        Actual = self.SavannaAviary.RemoveAnimalFromAviary(self.Tiger2)
        self.assertEqual(Expected, Actual)

    def testErrorIncorrectNeighborWhenAddAnimalToAviary(self):
        self.testAddAnimalToAviary()
        Expected = False
        Actual = self.SavannaAviary.AddAnimalToAviary(self.Elefant)
        self.assertEqual(Expected, Actual)

    def testErrorHaveNotAvailableSquareWhenAddAnimalToAviary(self):
        self.SavannaAviary.square = 1
        Expected = False
        Actual = self.AddAnimalToAviary(self.Elefant)
        self.assertEqual(Expected, Actual)

    def testErrorRemoveAnimalFromAviary(self):
        self.testSecondAddAnimalToAviary()
        Expected = False
        Actual = self.SavannaAviary.RemoveAnimalFromAviary(self.Elefant)
        self.assertEqual(Expected, Actual)

    def testFeedAnimalsInAviary(self):
        self.AddAnimalToAviary(self.Elefant)
        Expected = 20
        self.SavannaAviary.FeedAnimalsInAviary()
        Actual = self.SavannaAviary.animalsInAviary[0].alreadyEated
        self.assertEqual(Expected, Actual)
