class User:

    def __init__(self, username, role):
        self.username = username
        self.role = role

# 定义普通函数
# def create_user(username, role):
# 要求返回
# User(
#     username=username,
#     role=role
# )
def create_user(username, role):
    return User(username=username, role=role)

# 调用
# user = create_user(
#     username="test_user",
#     role="tester"
# )
# 打印
# print(type(user))
# print(user.username)
# print(user.role)

user = create_user(username="test_user", role="tester")
print(type(user))
print(user.username)
print(user.role)



# Q1:
# create_user() 返回的是什么类型的数据？
# A: 返回的是User对象

# Q2:
# 为什么返回对象之后还能继续访问
# user.username 和 user.role？
# A: creat_user() 返回一个User类型的对象，这个对象自带了username和role两个属性，
# 所以可以直接使用user.username和user.role来去访问对象的属性