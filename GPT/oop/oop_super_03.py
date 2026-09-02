class User:
    def __init__(self, username):
        self.username = username


class AdminUser(User):
    def __init__(self, username, level):
        super().__init__(username)
        self.level = level


admin = AdminUser(username="admin01", level=10)
print(admin.username)
print(admin.level)

# Q1:
# super().__init__(username)
# 调用的是哪个类的 __init__？
# A: 调用的是User类的__init__

# Q2:
# 为什么 AdminUser 不需要自己再写
# self.username = username？
# A: 因为父类的构造方法中已经包含了该内容，子类不需要重新写一遍，只需要使用super().__init__(username)调用一下就好了

# Q3:
# AdminUser 最终为什么同时拥有
# username 和 level 两个属性？
# A: 因为父类就有一个username属性，所以子类也会有，并且level是子类额外定义的一个属性，
# 所以AdminUser有username和level两个属性