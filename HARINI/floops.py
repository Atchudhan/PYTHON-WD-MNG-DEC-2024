fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 

for x in range(6):
    print(x)
else:
  print("Finally finished!")




for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")





adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)





























def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(food):
    for x in food:
        print(x)
fruits=["apple","banana","cherry"]
my_function(fruits)


def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(9))



def my_function(x, /):
  print(x)
my_function(3)


def my_function(x):
  print(x)
my_function(x = 3)


def my_function(*, x):
  print(x)
my_function(x = 3)



def my_function(x):
  print(x)
my_function(3)


def my_function(a, b, /, *, c, d):
  print(a + b + c + d)
my_function(5, 6, c = 7, d = 8)





def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("Recursion Example Results:")
tri_recursion(6)



















x=lambda a:a+10
print(x(5))


def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
















class MyClass:
    x=5
print(MyClass)




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
