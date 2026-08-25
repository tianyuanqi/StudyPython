## 函数
如果某段代码经常重复使用，那可以把这段代码封装起来

例如一个测试脚本，有100个测试账号，每个账号都需要访问数据库查询账号密码是否正确
那么可以直接把登录功能写成一个
```python
def login(username, password):
    user = findUserByUsername(username)  # 访问数据库去查询用户信息
    if user:
        if password == user.password:
            return "登录成功"
        else:
            return "登录失败,账号或密码错误"
    else:
        return "登录失败，账号或密码错误"


def findUserByUsername(username):  # 伪代码，调用数据库查询账户是否存在
    #去数据库查询相同username的用户
    #如果找到，返回用户信息
    #如果没找到，返回空
    return 用户信息或空

# 测试数据
test_cases=[{
    "username":"allen",
    "password":"123456"
},{
    "username":"yuanqi",
    "password":"123456"
},{
    "username":"admin",
    "password":"123456"
    }]

# 遍历测试数据，循环调用登录函数
for i in  test_cases:
    login(i["username"],i["password"])
```

## 形参和实参
在定义函数时，声明调用函数时必须传入的参数是形参
在调用函数时候，实际传入的叫做实参

```python

def login(username, password):  
    # 声明调用login函数时，比如传入两个参数，多一个少一个都无法成功调用
    return "登录成功或失败"
login()

login("allen", "123456")  # 这里调用login函数，传入的allen和123456就是实参
login() # 如果不传参数，或者传多了传少了，执行时都会报错
```

## 默认参数
* 在声明函数时，可以对形参设置默认参数
* 设置好默认参数后，调用该函数时可不传参数直接调用
* 如果设置了默认参数，调用函数时也传了参数，以调用函数时传入的实参为准
```python

def send_request(method,url,timeout=5):
    pass

send_request("post","/login") #因为timeout设置了默认参数，不传timeout参数也可调用
send_request("post","/login",10) #这里函数执行的时候，timeout为10
```



## 函数的作用域：
* 在函数内部定义的变量，作用域只是在函数内部，叫做局部变量
* 在函数外面定义的变量，作用域是整个.py文件，叫做全局变量

```python
token = "abc123"  # 全局变量，作用域是整个.py文件


def login():
    token = "123456"  # 局部变量，作用域是login函数内部
    print(token)


login()  # 输出123456
print(login())  # 输出"abc123"
```