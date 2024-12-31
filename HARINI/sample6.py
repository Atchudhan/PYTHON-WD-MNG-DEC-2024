#Convertir list en tuple
thistuple=("apple,","banana","cherry")
y=list(thistuple)
print(y)

#Ajout d'un élément dans la liste puis covertir en tuple
y.append("orange")
thistuple=tuple(y)
print(thistuple)


#Retirer un élément d'un tuple, on covertit en list, on retire l'élement puis on le reconvertir en tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)





fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)



fruits=("apple","banana","cherry","strawberry","raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)



fruits=("apple","mango","papaya","pineapple","cherry")
(green,*tropic,red)=fruits
print(green)
print(tropic)
print(red)




fruits = ("apple", "banana", "cherry")
fruits = ("green", "yellow", "red")
print(green)
print(yellow)
print(red)



fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
