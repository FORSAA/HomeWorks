from ImportAllClasses import *  #разовый импорт всех классов

FirstMyNewElefant = ElefantClass("Степан")
SecondMyNewElefant = ElefantClass("Ваня")
ThirdMyNewElefant = ElefantClass("Кирилл")
"""
print(MyNewElefant.animalType)

print(MyNewElefant.name)

print(MyNewElefant.age)

print(MyNewElefant.mass)

print(MyNewElefant.sound)

print(MyNewElefant.lifeSquare)

print(MyNewElefant.foodType)

if(MyNewElefant.isPredator == False):
    print("Не хищник")
else:
    print("Хищник")

if(MyNewElefant.isWannaEat == False):
    print("Не хочет есть")
else:
    print("Хочет есть")

print(MyNewElefant.biom)

MyNewElefant.GoEat(foodType="Мясо", foodMass=50)
"""

Aviary=SavannaAviary(name="1", canContainPredator=False)

Aviary.aviarySquare = 40
print("Площадь вольера: ", Aviary.aviarySquare, "m²", sep="")


Aviary.maxAnimalsInAviary = 5

Aviary.AddAnimalToAviary(FirstMyNewElefant)

Aviary.AddAnimalToAviary(SecondMyNewElefant)

Aviary.AddAnimalToAviary(ThirdMyNewElefant)

Aviary.RemoveAnimalFromAviary(FirstMyNewElefant)

Aviary.AnimalsDoSound()
