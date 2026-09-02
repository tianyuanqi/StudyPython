class BaseApi:
    def request(self):
        print("发送通用请求")


class LoginApi(BaseApi):
    def request(self):
        print("发送登录请求")


class UserApi(BaseApi):
    def request(self):
        super().request()
        print("附加用户接口处理")


base_api = BaseApi()
login_api = LoginApi()

base_api.request()
login_api.request()

user_api = UserApi()
user_api.request()

# Q1:
# LoginApi 中重新定义 request()
# 这种行为叫什么？
# A: 重写

# Q2:
# login_api.request()
# 为什么没有执行 BaseApi 中的 request()？
# A: 因为LoginApi中重写了request()方法，所以其对象只会调用重写后的子类方法

# Q3:
# UserApi.request() 中为什么又会执行
# BaseApi.request()？
# A: 因为UserApi在重写request()方法时又调用了父类的request方法，然后额外加上了子类的处理
# 所以会执行BaseApi.request()
