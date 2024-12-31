#Afficher en colonne
thislist=["apple","banana","cherry"]
for x in thislist:
        print(x)

        
thislist1=["apple","banana","cherry"]
for i in range(len(thislist1)):
    print(thislist1[i])




thislist2 = ["apple","banana","cherry"]
i = 0
while i<  len(thislist):
        print(thislist2[i])
        i = i + 1

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]




#Créer une liste à partir d'une autre liste
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
    print(newlist)




fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
print(newlist)




#Liste avec une condition
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if x!="apple"]
print(newlist)


fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits]
print(newlist)

#Afficher nombre
newlist=[x for x in range(10)]
print(newlist)

#Afficher nombre sous condition
newlist=[x for x in range(10) if x<5]
print(newlist)

#Afficher en majuscule
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x.upper()for x in fruits]
print(newlist)

#Remplacer une élément par un autre élément dans une autre liste
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x if x!="banana" else "orange" for x in fruits]
print(newlist)


#Ranger par ordre alphabétique
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


#Ranger par ordre croissant
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)


#Ranger par ordre alphabétique décroissant
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)


#Ranger par ordre décroissant
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)




def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#Copier une liste dans une autre liste
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist=thislist.copy()
print(mylist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist=list(thislist)
print(mylist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
myslist=thislist[:]
print(mylist)



#Joindre deux listes
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)




list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)




list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)


