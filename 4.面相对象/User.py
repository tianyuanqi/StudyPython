# 创建一个类
class User:

    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel

    def __gt__(self, other):
        return self.age > other.age

# 创建一个对象
user1 = User(name="杰克马", age=60, tel=1234567)
user2 = User(name="刘老板", age=59, tel=1234567)

print(user1 > user2)


