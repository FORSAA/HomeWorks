import unittest
from TigerClass import TigerClass
from ElefantClass import ElefantClass
from PenguinClass import PenguinClass

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.Penguin = PenguinClass("Пингвин")
        self.Elefant = ElefantClass("Слон")
        self.Tiger = TigerClass("Тигр")

    def testIsWannaEatPenguin(self):
        self.Penguin.GoEat(foodMass=50)
        expected = 50
        actual = self.Penguin.alreadyEated
        self.assertEqual(expected, actual)

    def testIsWannaEatElefant(self):
        self.Elefant.GoEat(foodMass=50)
        expected = 50
        actual = self.Elefant.alreadyEated
        self.assertEqual(expected, actual)


    def testIsWannaEatTiger(self):
        self.Tiger.GoEat(foodMass=50)
        expected = 50
        actual = self.Tiger.alreadyEated
        self.assertEqual(expected, actual)
