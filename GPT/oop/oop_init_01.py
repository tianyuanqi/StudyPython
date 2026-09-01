class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role


user1 = User(username="test_user", password="123456", role="tester")
user2 = User(username="admin", password="abcdef", role="admin")

print(user1.username)
print(user1.role)
print(user2.username)
print(user2.role)

# Q1:
# __init__ 在什么时候自动执行？
# A: 在初始化（创建实例）的时候自动执行

# Q2:
# self 表示什么？
# A: 表示这个对象本身

# Q3:
# 下面代码中：
#
# self.username = username
#
# 左边的 self.username 和右边的 username
# 分别是什么？
# A: 右边的username代表传入的实参，左边的self.username代表实例本身的属性，
# self.username=username是根据传入的参数给该实例赋值
