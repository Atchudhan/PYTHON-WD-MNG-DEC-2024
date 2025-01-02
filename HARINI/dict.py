thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)



thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])


thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)



thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x=thisdict["model"]
print(x)


thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x=thisdict.get("model")
print(x)

thisdict=   {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x=thisdict.keys()
print(x)






car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) 
car["color"] = "white"
print(x)




cdisdict = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=thisdict.values()
print(x)





car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) 
car["year"] = "2020"
print(x)



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) 
car["color"] = "red"
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x=thisdict.items()
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
print(x)


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["year"] = 2020
print(x) #after the change



car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
car["color"] = "red"
print(x) #after the change




thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)






child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)





myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])







myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])