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

# How to accept arguments from the command line in python

""" import sys

print(sys.argv[5])   # 访问第6个元素 """

# Lambda Function

""" lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2, 4)) """

# map(), filter(), reduce()

""" numbers = [1, 2, 3]

def double(a):
    return a * 2

result = map(double, numbers)

print(list(result)) """

# ---

""" numbers = [1, 2, 3]

double = lambda a : a * 2

result = map(double, numbers)

print(list(result)) """

# --- filter

""" numbers = [1, 2, 3, 4, 5, 6, 7, 8]

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result)) """

# !--- reduce()
""" from functools import reduce

expenses = [
    ('Dinner', 80),
    ('Car repair', 120)
]

sum = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum) """

# Recursion

""" def factorial(n):
    if n ==1: return 1
    return n * factorial(n-1)

print(factorial(3)) """

# Decorators

""" def logtime(func):
    def wrapper():
        print("before")
        val = func()
        print("after")
        return val
    return wrapper

@logtime
def hello():
    print("hello")

hello() """

# Docstrings

""" def increment(n):
 
    return n + 1

class Dog:
  
    def __init__(self, name, age):
   
        self.name = name
        self.age = age

    def bark(self):
       
        print('WOF!')

print(help(Dog)) """

# Annotations

""" def increment(n: int) -> int: 
    return n + 1

count: int = 0 """

# Exception

""" try:
    result = 2 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')
finally:
    result = 1

print(result) # 1 """

# ---

""" try:
    raise Exception('An error!')
except Exception as error:
    print(error) """

# ---

""" class DogNotFoundException(Exception):
    print("inside")
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
        print('Dog no found!') """

# With

""" filename = '/Users/flavio/test.txt'

with open(filename, 'r') as file:
    content = file.read()
    print(content) """

# pip

# List Compressions

""" numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

numbers_power_2 = []
for n in numbers:
    numbers_power_2.append(n**2) """

# Polymorphism

""" class Dog:
    def eat(self):
        print('Eating dog food')

class Cat:
    def eat(self):
        print('Eating cat food')

animal1 = Dog()
animal2 = Cat()

animal1.eat()
animal2.eat() """

# Operater Overloading

""" class Dog:
    # the Dog class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __gt__(self, other):
        return True if self.age > other.age else False

roger = Dog('Roger', 8)
syd = Dog('Syd', 7)

print(roger > syd) """

# --- And now....

""" __add__() respond to the + operator
__sub__() respond to the - operator
__mul__() respond to the * operator
__truediv__() respond to the / operator
__floordiv__() respond to the // operator
__mod__() respond to the % operator
__pow__() respond to the ** operator
__rshift__() respond to the >> operator
__lshift__() respond to the << operator
__and__() respond to the & operator
__or__() respond to the | operator
__xor__() respond to the ^ operator
 """