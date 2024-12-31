i=1
while i<6:
    print(i)
    i+=1

    
i = 1
while i < 6:
    print(i)
    if(i == 3):
        break
    i+=1





#Même méthode.Reviens à dire la même chose    
thislist=["apple","banana","cherry"]
for i in range(len(thislist)):
    print(thislist[i])

thislist=["apple","banana","cherry"]
for i in range(3):
    print(thislist[i])







thislist = ["banana","Kiwi", "cherry","apple"]
thislist.reverse()
print(thislist) 

thislist = ["banana","Kiwi", "cherry","apple","Watermelon","Orange"]
thislist.reverse()
print(thislist) 







thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
