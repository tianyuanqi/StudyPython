## 继承的核心是：复用
定义一个父类`class BaseApi()` <br>
然后再定义一个子类，`class LoginApi(BaseApi)`<br>
在括号中写入父类的名称，即可代表继承自该父类

##子类可以继承父类中可继承的属性和方法，也可以在此基础上新增自己的属性和方法，并可以重写父类的方法。<br>
继承类 ≠ 凭空自动产生所有实例属性
执行初始化代码 → 才把实例属性保存到具体对象中


## 重写
若父类提供的方法不能满足子类需求（或者不适用），子类可以将其进行重写<br>
例如父类的方法名叫`request()`,子类在定义时，也声明一个`request()`方法，即表示对父类的同名方法进行了重写


## `Super()`，在子类中调用父类的实现
例如父类中有一个init方法用于初始化
然后有一个子类，也需要一个init方法用于初始化，然后额外传入一个参数作为子类特有的属性


```python
class BaseApi():  # 父类Api
    def __init__(self, url, timeout=5):
        self.url = url
        self.timeout = timeout


class LoginApi(BaseApi):
    def __init__(self, url, timeout, username, password):
        super().__init__(url, timeout) 
        #使用super方法去调用父类的init，就不用再写self.url=url以及self.timeout=timeout了
        
        self.username = username
        self.password = password
        
login_test=LoginApi("http://2400px",timeout=5,username="admin",password="123456")

```

这时候就可以使用`super().__init__(base_url)`


父类负责公共内容，子类负责自己的特殊内容
例如：
```python
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

```
运行结果
```text
接口访问的地址为:http://2400px/api/login
登陆成功
接口访问的地址为:http://2400px/api/user
{'userId': 1001, 'userName': 'jackma', 'role': 'admin', 'age': 30}
```
这里把接口路径的拼接做到了BaseApi中，在其子类UserApi以及LoginApi中，就不需要重复去拼接访问路径了

