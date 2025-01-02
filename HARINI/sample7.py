thisset={"apple","cherry","banana"}
print(thisset)



thisset={"apple","cherry","banana",True,1}
print(thisset)



thisset={"apple","cherry","banana",1,True}
print(thisset)


thisset={"apple","cherry","banana",1,True}
print(len(thisset))



thisset=set(("apple","banana","cherry"))
print(thisset)


thisset={"apple","cherry","banana"}
for x in thisset:
    print(x)

thisset={"apple","cherry","banana"}
print("banana" in thisset)



thisset={"apple","cherry","banana"}
print("banana" not in thisset)




thisset={"apple","cherry","banana"}
thisset.add("strawberry")
print(thisset)



thisset={"apple","cherry","banana"}
tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)






set1={"one","two","three"}
set2={1,2,3}
set3=set1.union(set2)
print(set3)


set1={"one","two","three"}
set2={1,2,3}
set1.update(set2)
print(set1)



set1={"one","two","three"}
set2= {1,2,3}
set3 = set1 | set2
print(set3)





set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)
