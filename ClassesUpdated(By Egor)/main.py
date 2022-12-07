from ImportAllClasses import * #разовый импорт всех классов

MyNewElefant = ElefantClass("Степан")
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

aviary = BaseAviary(name="1")
aviary.AddAnimalToAviary(MyNewElefant)
