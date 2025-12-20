""" def make_greeter(name):
    def greet():
        print(f"你好，{name}！")
    return greet

# 创建两个不同的问候器
greet_xiaoming = make_greeter("小明")
greet_xiaohong = make_greeter("小红")

greet_xiaoming()  # 输出：你好，小明！
greet_xiaoming()  # 输出：你好，小明！
greet_xiaohong()  # 输出：你好，小红！
 """
# ---

""" def create_piggy_bank():
    money = 0
    
    def save(amount):
        nonlocal money
        money = money + amount
        print(f"save {amount}$, rest {money}$")
    
    return save

my_bank = create_piggy_bank()

my_bank(100)
my_bank(50)
my_bank(30) """

# ---

""" def make_mutiplier(n):
    def mutiply(x):
        return x * n
    return mutiply

double = make_mutiplier(2)
triple = make_mutiplier(3)

print(double(5))
print(double(9))
print(triple(5)) """

# ---class
""" 
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def introduce(self):
        print(f"我叫{self.name}, 我读{self.grade}年级") 

# 创建两个学生
xiaoming = Student("小明", 3)
xiaohong = Student("小红", 5)

# 让他们自我介绍
xiaoming.introduce() # 输出：我叫小明，我读三年级
xiaohong.introduce() # 输出：我叫小红，我读五年级 """

# ---

""" class Phone:
    def __init__(self, brand):
        self.brand = brand

    def call(self, number):
        print(f"用{self.brand}打电话给{number}")

# 创建两部手机
my_phone = Phone("苹果")
your_phone = Phone("小米")

# 打电话
my_phone.call("110")
your_phone.call("120") """

# ---

class Account:
    def __init__(self, owner, money):
        self.owner = owner
        self.money = money

    def deposit(self, amount):
        self.money = self.money + amount
        print(f"{self.owner}存了{amount}元，余额{self.money}元")

# 开户
zhang_san = Account("张三", 100)

# 存钱
zhang_san.deposit(50)
zhang_san.deposit(30)