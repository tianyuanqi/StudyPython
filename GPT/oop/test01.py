BASE_URL = "http://2400px/api"  # 作为配置项，项目的基础地址


class BaseApi:
    def __init__(self, timeout=5):
        self.base_url = BASE_URL
        self.timeout = timeout

    def build_url(self, path):
        return self.base_url + path


class UserApi(BaseApi):
    def get_user_info(self, userid):
        url = self.build_url("/user")
        print(f"接口访问的地址为:{url}")
        # 伪代码，根据用户id去查询信息findUserById（userid）

        return {
            "userId": userid,
            "userName": "jackma",
            "role": "admin",
            "age": 30
        }


class LoginApi(BaseApi):
    def login(self, username, password):
        url = self.build_url("/login")
        print(f"接口访问的地址为:{url}")
        if username == "user" and password == "123456":
            return "登陆成功"
        else:
            return "登录失败"


# 调用登录接口
login_result = LoginApi().login(username="user", password="123456")
print(login_result)

# 调用用户信息接口
user_result = UserApi().get_user_info(1001)
print(user_result)
