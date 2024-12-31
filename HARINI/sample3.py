thislist=["apple","banana","cherry"]
print(thislist)



thislist=["apple","banana","apple","cherry"]
print(thislist)


thislist=["apple","banana","cherry"]
print(len(thislist))

thislist=list(("apple","banana","cherry"))
print(thislist)



thislist=["apple","banana","cherry"]
print(thislist[1])

thislist=["apple","banana","cherry"]
print(thislist[-1])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[:5])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[-5:-2])


thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruitrs list")


#Remplacement du 2
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[2]="blackcurrant"
print(thislist)



#Remplacement du 1 et 2
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:3]=["blackcurrant","watermelon"]
print(thislist)


#Ajouts + on garde position du 2
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:2]=["blackcurrant","watermelon"]
print(thislist)


#Ajout + suppression du 1 et 2
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist[1:3]=["watermelon"]
print(thislist)


#Insertion
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist.insert (2,"watermelon")
print(thislist)

#Ajout à la fin
thislist=["apple","banana","cherry","orange","kiwi","melon","mango"]
thislist.append ("watermelon")
print(thislist)


#Ajout d'une liste dans une autre liste
thislist=["apple","banana","cherry"]
tropical=["mango","pineapple","papaya"]
thislist.extend(tropical)
print(thislist)


#Retirer un élément
thislist=["apple","banana","cherry"]
thislist.remove("banana")
print(thislist)


#Retrait du 1er élément lorsque l'élément est répété
thislist=["apple","banana","cherry","banana"]
thislist.remove("banana")
print(thislist)

#Retrait d'un élément par numérotation
thislist=["apple","banana","cherry"]
thislist.pop(1)
print(thislist)

#Retrait du dernier élément
thislist=["apple","banana","cherry"]
thislist.pop()
print(thislist)

#Effacer un élément
thislist=["apple","banana","cherry"]
del thislist[0]
print(thislist)

#Effacer la liste entière
thislist2=["apple","banana","cherry"]
del thislist2
print(thislist2) 

#"Dégager" une liste
thislist=["apple","banana","cherry"]
thislist.clear()
print(thislist)










