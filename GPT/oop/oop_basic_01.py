class User:
    pass

user1 = User()
user2 = User()

print(type(user1))
print(type(user2))

print(user1 is user2)
# Q1:
# class 是什么？
# A: class是一个类，类是一类东西的抽象，比如人类（并不具体指某个人），用户（并不具体指某个账号）

# Q2:
# 对象（实例）是什么？
# A: 对象是类的一个具体的实例（个体），比如类是人类，对象就是詹姆斯，或者梅西，也可以是其他人（具体的一个人）

# Q3:
# user1 和 user2 都来自 User 类，
# 为什么 user1 is user2 是 False？
# A: 因为user1和user2是两个不同的实例，他们在内存中有各自的地址