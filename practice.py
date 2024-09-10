print("halaoppah") #This is my name

if 5 > 9:
    print("Five is greater than nine")
if 5 < 9:
    print("Five is less than nine") 

x = 5
y = 9
print(x+y)

x = "Oppah"
x = 5
print(x)

x = str(3)
y = int(2)
z = float(3)
print(y+z)

x = 5
y = 'Oppah'
print(type(x))
print(type(y))

x, y, z = "Enoch", "Oppah", "Daniel"
print(x)
print(y)
print(z)

Car = ["Range Rover", "Toyota Pick Up", "Benz"]
x, z, y = Car
print(z)
print(y)
print(x)

x = "Python"
y = "is"
z = 9
print(x, y, z)

x = "Awesome"
def myFunction():
    print("Python is " + x)
myFunction()

x = "Awesome"
def myFunction():
    x = "Fantastic"
    print("Python is " + x)
myFunction()

print("Python is " + x)

x = 2+1j
print(x)

x = ["Man", "Woman"]
print(x)

x = ("Man", "Woman")
print(x)

y = range(1, 10)
print(y)

y = {"Age" : 20, "Name" : "Ama"}
print(y)

x = 10+5j
print(x)

x = 2
x = float(x)
print(x)

x = float("3")
print(x)

print("'OPPAH'")

x = "oppah"
print(x[3])

for x in "banana":
    print(x)

x = "banana"
print(len(x))

txt = "Oppah is learning Python"
if "Oppah" in txt:
    print("Oppah is present")

txt = "The man"
print(txt[-2:-1])
print(txt.upper())
print(txt.replace('m', 'M'))
print(txt.lower())
print(txt.capitalize())


age = 32
txt = f"My name is oppah and I am {age * 2} years old"
print(txt)

price = 50
txt = f"The price of the watch is {price: .2f} pounds"
print(txt)

x = "hello"
print(bool(x))
print(bool(5))
print(isinstance(x, str))

print(x := 3)

thelist = ["me", 5, "when", "2.0", "see"]
thelist1 = [2, 5, 8]
thelist.extend(thelist1)
thelist[1] = "see"
thelist.append("it")
thelist.insert(3, "in")
print(thelist)
print(len(thelist))
print(thelist[-2])
print(thelist[2:4])
print(thelist)
thelist.remove("see")
print(thelist)
thelist.pop()
print(thelist)
del thelist[3]
print(thelist)
thelist.clear()
print(thelist)

thelist = ["me", 5, "when", "2.0", "see"]
for x in thelist:
    print(x)

thelist = ["me", 5, "when", "2.0", "see"]
for i in range(len (thelist)):
    print(thelist[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

thelist = ["me", "when", "see"]
thelist.sort(reverse=True)
print(thelist)

thelist = ["me", "when", "see"]
mylist = thelist.copy()
print(mylist)

thelist = ("me",)
print(type(thelist))

thislist = ("me", "You")
y = list(thislist)
y.append("Sex")
print(y) 

(me, You) = thislist
print(me)
print(You) 

thisset = {"jon", "lee", "lee"}
print(thisset)

thisset = {"jon", "lee", 1, True}
thisset.add("Kill")
print(thisset)
print(len(thisset))

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
##set3 = set1 | set2
set3 = set1.union(set2)
print(set3)

thisdict = {
    "Name": "Toyota",
    "Brand": "Hilux",
    "Year": 2024
}

thisdict ["Color"] = "White"
mydict = thisdict.copy()

print(thisdict["Year"])
print(thisdict)
print(mydict)

a = 200
b = 33

if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

a = 50
b = 30
c = 10

if a > b and b > c:
    print("Both conditions are true")
  
fruits = ["Apple", "Grapes", "Guava"]
for x in fruits:
    if x == "Grapes":
        continue
    print(x)

for x in range(2, 6, 2):
    print(x)

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished")

def myFunction(fName):
    print(fName + " Oppah")
myFunction("Enoch")
myFunction("Daniel")

def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Joe", "Linus", "Oppah")

def myFunction(x):
    return 5 * x
print (myFunction(4))

x = lambda a, b : a + b + 10
print(x(3, 4))

def myfunction(n):
    return lambda a: a * n
mydoubler = myfunction(2)
print(mydoubler(11))

x = 5

def myfunction():
    x = 200
    print(x)
myfunction()
print(x)

import datetime
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime("%b"))
print(x.strftime("%a"))
print(x.strftime("%B"))

y = datetime.datetime(2024, 3, 25)
print(y)

x = min(2, 5 , 4)
y = max(2, 5 , 4)
d = abs(-2.35)
a = pow(2, 3)
print(x)
print(y)
print(d)
print(a)

import math
x = math.ceil(25.9)
y = math.floor(25.9)
z = math.sqrt(64)
print(x)
print(y)
print(z)

import json
## Converting JSON to Python
x = '{"name" : "Enoch", "age" : 30, "City" : "Cape Coast"}'
y = json.loads(x)
print(y["name"])

## Converting Python to JSON
x = {"name" : "Enoch", "age" : 30, "City" : "Cape Coast"}
y = json.dumps(x)
print(y)

import re
txt = "I am Handsome"
x = re.findall("am", txt)
print(x)

txt = "It a beautiful day"
x = re.search("^It.*day$", txt)
print(x)

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

try:
    x = 50
    y = 10
    if x > y:
        print("Yes")
except:
    print("Something is wrong with your head")

username = input()
if username == str():
    print("Yello")
else:
    print("Geez")

price = 50000
txt = f"I have to pay a price of {price:,}"
print(txt)


