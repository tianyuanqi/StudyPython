class BaseApi:
    def __init__(self, base_url, timeout=5):
        self.base_url = base_url
        self.timeout = timeout

    def build_url(self, path):
        return self.base_url + path


class LoginApi(BaseApi):
    def login(self, username, password):
        url = self.build_url("/login")

        return {
            "url": url,
            "timeout": self.timeout,
            "username": username,
            "password": password
        }


class UserApi(BaseApi):
    def get_user_info(self, user_id):
        url = self.build_url("/user")

        return {
            "url": url,
            "timeout": self.timeout,
            "user_id": user_id
        }


login_api = LoginApi(base_url="http://api.test.com", timeout=10)

user_api=UserApi(base_url="http://api.test.com")

login_result=login_api.login(username="test_user",password="123456")

user_result=user_api.get_user_info(user_id=10001)
print(login_result)
print(user_result)

# Q1:
# LoginApi 和 UserApi 为什么都可以使用
# self.base_url 和 self.timeout？
# A: 因为它们都是BaseApi的子类，子类默认具有父类的属性

# Q2:
# build_url() 为什么只需要在 BaseApi 中写一次？
# A: 因为子类同样继承了父类的方法，子类对象同样可以调用build_url()

# Q3:
# login_api 和 user_api 是否是同一个对象？
# A: 不是同一个对象，它们属于不同的子类对象

# Q4:
# 这里使用继承的主要目的是什么？
# A: 让代码重复使用，不需要在每个子类中都重复的去定义url属性，重复去拼接口地址