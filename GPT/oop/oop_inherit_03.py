class BaseApi:
    def __init__(self, base_url):
        self.base_url = base_url

    def show_base_url(self):
        print(f"base_url:{self.base_url}")


class LoginApi(BaseApi):
    def login(self):
        print("执行登录接口")


login_api = LoginApi("http://api.test.com")
login_api.show_base_url()
login_api.login()

print(isinstance(login_api, LoginApi))
print(isinstance(login_api, BaseApi))

# Q1:
# BaseApi 和 LoginApi 分别是什么关系？
# A: 继承关系，LoginApi是BaseApi的子类

# Q2:
# LoginApi 中没有定义 show_base_url()，
# 为什么 login_api 仍然可以调用？
# A: 因为login_api是LoginApi的实例，而LoginApi继承自BaseApi，BaseApi里面有show_base_url()方法，
# 子类的实例可以调用父类的方法

# Q3:
# 为什么 isinstance(login_api, BaseApi)
# 也是 True？
# A: 因为login_api也属于BaseApi体系下的一个对象
