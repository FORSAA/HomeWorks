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
print("\n")
FirstMyNewElefant.GoEat(foodType="Мясо", foodMass=50)
print("\n")
# FirstMyNewElefant.GoEat(foodType="Бананы", foodMass=50)
print("\n")
NewAviary = SavannaAviary(AviaryName="Вольер1", biom="Саванна")
print(f"{NewAviary.aviaryName} был успешно создан")
NewAviary.maxAnimalsInAviary = 5
NewAviary.square = 50
print("\n")
NewAviary.AddAnimalToAviary(FirstMyNewElefant)
print("\n")
NewAviary.AskWhoWannaEat()
print("\n")
NewAviary.FeedAnimalsInAviary()
print("\n")
NewAviary.AskWhoWannaEat()
print("\n")
NewAviary.AnimalsDoSound()
print("\n")
NewAviary.AddAnimalToAviary(FirstMyNewTiger)
print("\n")
NewAviary.RemoveAnimalFromAviary(FirstMyNewElefant)
print("\n")
print(NewAviary.animalsInAviary)