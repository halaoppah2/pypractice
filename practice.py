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
