from ImportAllClasses import *  #разовый импорт всех классов

MyNewElefant = ElefantClass("Степан")
MyNewElefantA = ElefantClass("Ваня")
MyNewElefantB = ElefantClass("Кирилл")
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

A=SavannaAviary(name="1", canContainPredator=False)

A.aviarySquare = 40
print("Площадь вольера: ", A.aviarySquare, "m²", sep="")


A.maxAnimalsInAviary = 5

A.AddAnimalToAviary(MyNewElefant)

A.AddAnimalToAviary(MyNewElefantA)

A.AddAnimalToAviary(MyNewElefantB)

A.RemoveAnimalFromAviary(MyNewElefant)

A.AnimalsDoSound()
