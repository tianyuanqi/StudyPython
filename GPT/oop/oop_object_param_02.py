class User:

    def __init__(self, username, status):
        self.username = username
        self.status = status


def disable_user(user):
    user.status = "disabled"


user = User(
    username="test_user",
    status="enabled"
)

print(user.status)
disable_user(user)
print(user.status)

# Q1:
# 把 user 对象传给 disable_user() 时，
# 函数里面是否重新创建了一个新的 User 对象？
# A:没有新建一个User对象，修改的是原本已存在的对象user

# Q2:
# 为什么函数里的
#
# user.status = "disabled"
#
# 会影响函数外面的原对象？
# A: 因为函数里面的形参user，和函数外的user是同一个对象，函数没有重新创建对象，所以修改的是原本对象的属性

# Q3:
# 如果函数中只是：
#
# print(user.status)
#
# 会不会修改原对象？
# A:不会修改原对象，该函数只是把原本的status属性给打印到控制台上
