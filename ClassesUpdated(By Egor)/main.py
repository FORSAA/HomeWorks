
from ImportAllClasses import *  #разовый импорт всех классов
def DebugAnimalClass():
    print("-------ПРОВЕРКА КЛАССОВ ЖИВОТНЫХ--------")
    Elefant = ElefantClass(name="Алексей")
    print("Тип:", Elefant.animalType)
    print("Имя:", Elefant.name)
    print("Возраст:", Elefant.age)
    print("Вес:", Elefant.mass)
    print("Звук:", Elefant.sound)
    print("Жилая площадь:", Elefant.lifeSquare)
    print("Тип еды:", Elefant.foodType)
    print("Уже съел еды:", Elefant.alreadyEated)
    print("Нужно еды:", Elefant.foodPerDay)
    print("Биом:", Elefant.biom)
    print("\n")
    Elefant = TigerClass(name="Тимур")
    print("Тип:", Elefant.animalType)
    print("Имя:", Elefant.name)
    print("Возраст:", Elefant.age)
    print("Вес:", Elefant.mass)
    print("Звук:", Elefant.sound)
    print("Жилая площадь:", Elefant.lifeSquare)
    print("Тип еды:", Elefant.foodType)
    print("Уже съел еды:", Elefant.alreadyEated)
    print("Нужно еды:", Elefant.foodPerDay)
    print("Биом:", Elefant.biom)
    print("\n")
    Elefant = PenguinClass(name="Федя")
    print("Тип:", Elefant.animalType)
    print("Имя:", Elefant.name)
    print("Возраст:", Elefant.age)
    print("Вес:", Elefant.mass)
    print("Звук:", Elefant.sound)
    print("Жилая площадь:", Elefant.lifeSquare)
    print("Тип еды:", Elefant.foodType)
    print("Уже съел еды:", Elefant.alreadyEated)
    print("Нужно еды:", Elefant.foodPerDay)
    print("Биом:", Elefant.biom)

def DebugAviaryClass():
    print("-------ПРОВЕРКА КЛАССОВ ВОЛЬЕРОВ--------")
    FirstTestAnimal = ElefantClass("Степан")
    SecondTestAnimal = ElefantClass("Алексей")
    ThirdTestAnimal = ElefantClass("Алексей")
    FourthTestAnimal = TigerClass("Кирилл")

    print("\n")
    TestSavannaAviary = SavannaAviary("Вольер 1")
    print("\n")
    TestArcticAviary = SavannaAviary("Вольер 2")
    print("\n")

    TestSavannaAviary.square = 50
    TestArcticAviary.square = 50

    TestSavannaAviary.foodTank = 400
    TestArcticAviary.foodTank = 400

    TestSavannaAviary.maxAnimalsInAviary = 5
    TestArcticAviary.maxAnimalsInAviary = 5


    print("Название вольера:", TestSavannaAviary.aviaryName)
    print("Биом вольера:", TestSavannaAviary.biom)
    print("Площадь вольера:", TestSavannaAviary.square)
    print("Животные в вольере:", TestSavannaAviary.animalsInAviary)
    print("Количество животных в вольере:", TestSavannaAviary.animalsInAviaryInt)
    print("Количество еды в вольере:", TestSavannaAviary.foodTank)
    print("Максимальное количество зверей в вольере:", TestSavannaAviary.maxAnimalsInAviary)

    print("\n")
    print("Название вольера:", TestArcticAviary.aviaryName)
    print("Биом вольера:", TestArcticAviary.biom)
    print("Площадь вольера:", TestArcticAviary.square)
    print("Животные в вольере:", TestArcticAviary.animalsInAviary)
    print("Количество животных в вольере:", TestArcticAviary.animalsInAviaryInt)
    print("Количество еды в вольере:", TestArcticAviary.foodTank)
    print("Максимальное количество зверей в вольере:", TestArcticAviary.maxAnimalsInAviary)

    print("\n")
    TestSavannaAviary.AddAnimalToAviary(FirstTestAnimal)
    print("\n")
    TestSavannaAviary.AddAnimalToAviary(SecondTestAnimal)
    print("\n")
    TestSavannaAviary.AddAnimalToAviary(ThirdTestAnimal)
    print("\n")

    TestSavannaAviary.FeedAnimalsInAviary()
    print("\n")
    TestSavannaAviary.AskWhoWannaEat()
    print("\n")
    TestSavannaAviary.AnimalsDoSound()
    print("\n")

    TestSavannaAviary.RemoveAnimalFromAviary(FirstTestAnimal)
    print("\n")
    TestSavannaAviary.AddAnimalToAviary(ThirdTestAnimal)
    print("\n")
    TestSavannaAviary.AddAnimalToAviary(FourthTestAnimal)
    print("\n")

def ZooDebug():
    print("-------ПРОВЕРКА ФУНКЦИЙ ЗООПАРКА---------")
    FirstTestAnimal = ElefantClass("Степан")
    SecondTestAnimal = ElefantClass("Алексей")
    ThirdTestAnimal = TigerClass("Кирилл")


    print("\n")
    FirstTestSavannaAviary = SavannaAviary("Вольер 1")
    print("\n")
    SecondTestSavannaAviary = SavannaAviary("Вольер 2")
    print("\n")
    TestArcticAviary = SavannaAviary("Вольер 3")
    print("\n")

    FirstTestSavannaAviary.square = 50
    TestArcticAviary.square = 50
    SecondTestSavannaAviary.square = 50

    FirstTestSavannaAviary.foodTank = 400
    TestArcticAviary.foodTank = 400
    SecondTestSavannaAviary.foodTank = 400

    FirstTestSavannaAviary.maxAnimalsInAviary = 5
    TestArcticAviary.maxAnimalsInAviary = 5
    SecondTestSavannaAviary.maxAnimalsInAviary = 5

    TestZoo = BaseZooClass("Зоопарк 1")

    FirstTestSavannaAviary.AddAnimalToAviary(ThirdTestAnimal)
    SecondTestSavannaAviary.AddAnimalToAviary(SecondTestAnimal)

    TestZoo.AddAviaryToZoo(FirstTestSavannaAviary)
    print("\n")
    TestZoo.AddAviaryToZoo(SecondTestSavannaAviary)
    print("\n")
    # print("Список вольеров в зоопарке", TestZoo.aviaryList)
    print("Имя зоопарка", TestZoo.zooName)
    print("\n")
    TestZoo.TransferAnimalBetweenAviaries(FirstTestSavannaAviary.animalsInAviary[0], FirstTestSavannaAviary, SecondTestSavannaAviary)
    print("\n")
    TestZoo.AskWhoNeedFoodForAviaries()

ZooDebug()
