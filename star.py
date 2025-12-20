# Tuples
""" names = ("Roger", "Syd", "Beau")

names[-1]
names.index("Roger")

len(names)

print("Roger" in names)
print(sorted(names))
newTuple = names + ("Tina", "Quincy")  """

# Dictionary
""" dog = {"name": "Roger", "age": 8, "color": "green"}

dog["favourtie food"] = "Meat"

del dog['color']

dogCopy = dog.copy()

print(dog)
print(dogCopy) """

# Sets集合
""" set1 = {"Roger", "Syd"}
set2 = {"Roger"}

intersect = set1 - set2
print(intersect) """

# Function功能

""" def hello(name, age):
    print('Hello! ' + name + ", you are" + str(age) + " year old!") 

hello("Beau", 39) """

# ---

""" def change(value):
    value["name"] = "Syd"

val = {"name": "beau"}
change(val)

print(val) """

# ---

""" def hello(name):
    if not name:
        return name, "Beau", 8
    print('Hello ' + name + '!')

print(hello("Syd"))
 """

 # --· Variable Scope变量作用域

""" def test():
    age = 8
    print(age)

print(age) # 8
test() # 8 """

# --- !Nest Functions 嵌套函数

""" def talk(phrase):
    def say(word):
        print(word)

    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk') """

# ---

""" def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    increment()

count() """

# !Closures闭包

""" def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        print(count)

    return increment

increment = counter()

print(increment()) # 1
print(increment()) # 2
print(increment()) # 3 """

# Object

""" age= 8

print(age.real)
print(age.imag)
print(age.bit_length()) # bit_length method: returns the number of bits necessary to represent this number in binary notation """

# ---

""" items = [1, 2]
items.append(3)
items.pop()
print(id(items))

# PS: append 和 pop 都是"原地修改"，列表的 id 不会变！ """

# Loops: While & For循环

## while loop

""" count = 0
while count < 10:
    print("The condition is Ture")
    count = count + 1

print("After the loop") """

## for loop

""" items = ["Beau", "Syd", "Quincy"]
for index, item in enumerate(items):
    print(index, item) """

### break

""" items = [1, 2, 3, 4]
for item in items:
    if item == 2:
        continue # continue stops the current iteration and tells python to execute the next one
        break
    print(item) """

# !classes

""" class Animal: # inherent
    def walk(self):
        print("Walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark():
        print("woof!")

Roger = Dog("Roger", 8)

print(Roger.name)
print(Roger.age)

Roger.bark()
Roger.walk """

# Module模块（见Module文件夹）
