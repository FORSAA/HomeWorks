from ImportAllClasses import *  #разовый импорт всех классов

FirstMyNewElefant = ElefantClass("Степан")
SecondMyNewElefant = ElefantClass("Ваня")
ThirdMyNewElefant = ElefantClass("Кирилл")

FirstMyNewTiger = TigerClass("Алексей")
SecondMyNewTiger = TigerClass("Терентий")

print(FirstMyNewElefant.animalType)

print(FirstMyNewElefant.name)

print(FirstMyNewElefant.age, "лет")

print(FirstMyNewElefant.mass, "кг", sep='')

print(FirstMyNewElefant.DoSound())

print(FirstMyNewElefant.lifeSquare, "m²", sep='')

print(FirstMyNewElefant.foodType)

if(FirstMyNewElefant.isPredator == False):
    print("Не хищник")
else:
    print("Хищник")

if(FirstMyNewElefant.isWannaEat == False):
    print("Не хочет есть")
else:
    print("Хочет есть")

print(FirstMyNewElefant.biom)
print("\n")
FirstMyNewElefant.GoEat(foodType="Мясо", foodMass=50)
print("\n")
FirstMyNewElefant.GoEat(foodType="Бананы", foodMass=20)
print("\n")
print("---------Функции вольера--------")
NewAviary = SavannaAviary(AviaryName="Вольер1", biom="Саванна")
NewAviary.maxAnimalsInAviary = 5
NewAviary.square = 50
print("\n")
NewAviary.AddAnimalToAviary(FirstMyNewTiger)
print("\n")
NewAviary.AskWhoWannaEat()
print("\n")
NewAviary.foodTank = 400
print(NewAviary.foodTank, "кг еды в баках", sep='')
print("\n")
NewAviary.FeedAnimalsInAviary(foodType="Мясо", mass=30)
print("\n")
print(NewAviary.foodTank, "кг еды в баках", sep='')
print("\n")
NewAviary.AskWhoWannaEat()
print("\n")
NewAviary.AnimalsDoSound()
print("\n")
NewAviary.AddAnimalToAviary(FirstMyNewElefant)
print("\n")
NewAviary.AddAnimalToAviary(SecondMyNewTiger)
print("\n")
print(NewAviary.square, "m² доступно в вольере ", NewAviary.aviaryName, sep='')
print("\n")
NewAviary.RemoveAnimalFromAviary(FirstMyNewTiger)
print("\n")
print(NewAviary.square, "m² доступно в вольере ", NewAviary.aviaryName, sep='')