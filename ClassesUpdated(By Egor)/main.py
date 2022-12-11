from ImportAllClasses import *  #разовый импорт всех классов

FirstMyNewElefant = ElefantClass("Степан")
SecondMyNewElefant = ElefantClass("Ваня")
ThirdMyNewElefant = ElefantClass("Кирилл")

FirstMyNewTiger = TigerClass("Алексей")

print(FirstMyNewElefant.animalType)

print(FirstMyNewElefant.name)

print(FirstMyNewElefant.age, "лет")

print(FirstMyNewElefant.mass, "кг", sep='')

print(FirstMyNewElefant.sound)

print(FirstMyNewElefant.lifeSquare, "m²")

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

FirstMyNewElefant.GoEat(foodType="Мясо", foodMass=50)
print("\n")

Aviary=SavannaAviary(name="1", canContainPredator=True)

Aviary.aviarySquare = 40
print("Площадь вольера: ", Aviary.aviarySquare, "m²", sep="")
print("\n")
Aviary.maxAnimalsInAviary = 5

Aviary.AddAnimalToAviary(FirstMyNewElefant)
print("\n")
Aviary.AddAnimalToAviary(SecondMyNewElefant)
print("\n")
Aviary.AddAnimalToAviary(ThirdMyNewElefant)
print("\n")

Aviary.AddAnimalToAviary(FirstMyNewTiger)
print("\n")
Aviary.AskWhoWannaEat
Aviary.FeedAnimalsInAviary(20)
Aviary.AskWhoWannaEat
