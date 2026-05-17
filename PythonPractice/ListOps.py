Fruits=["Apple","Orange","Kiwi","Banana","Grapes"]
Veggies=["Spinach","Bottleguard"]

print("Fruits list: {}".format(Fruits))
print(Fruits)
print(Veggies)

print(Fruits[0])
print(Fruits[-1])
print(Fruits[::-1])
print(Fruits[-1::-1])
print(Fruits[0:3])

FruitsAndVeggies=Fruits+Veggies
print(FruitsAndVeggies)

Veggies.append("Snakeguard")
print(Veggies)

#list is mutable, means we can modify the lift once created
Veggies.insert(0,"Brinzal")
print(Veggies)

IsKiwiInFruits="Kiwi" in Fruits
print(IsKiwiInFruits)  # True

KiwiIndex=Fruits.index("Kiwi")
print(KiwiIndex)

lenOfFruits=len(Fruits)
print(lenOfFruits)

Fruits.pop()
print(Fruits)

Fruits.insert(0,"Banana")
print(Fruits)

Fruits.remove("Banana")
print(Fruits)

Fruits.pop(1)
print(Fruits)

