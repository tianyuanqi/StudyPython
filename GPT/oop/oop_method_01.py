class User:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == "test_user" and self.password == "123456":
            return True
        else:
            return False

    def show_username(self):
        print(f"当前用户:{self.username}")


def check_login(user):
    token = user.login()
    if token == True:
        print("登录成功")
    else:
        print("登录失败")


success_user = User("test_user", "123456")
failed_user = User("test_user", "wrong_password")

success_user.show_username()
check_login(success_user)

failed_user.show_username()
check_login(failed_user)

# Q1:
# 类中定义的函数通常叫什么？
# A: 方法

# Q2:
# 为什么调用：
#
# success_user.login()
#
# 时不需要手动给 self 传值？
# A: 通过对象调用实例方法时，Python 会自动把这个对象本身作为第一个参数传给 self,所以调用时不用手动传self