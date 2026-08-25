base_url = "https://api.test.com"


def show_base_url():
    # 在函数中打印全局变量base_url。
    print(base_url)


show_base_url()

print("————————————————分割线——————————————————")


def create_token():
    token = "abc123"
    return token


token = create_token()


def show_token(token):
    print(f"token:{token}")


show_token(token)

print("————————————————分割线——————————————————")
name = "global_name"


def change_name():
    name = "local_name"
    print(name)


change_name()
print(name)

# Q1: 什么是局部变量？
# A: 在函数内部定义，且只在函数内部生效的变量

# Q2: 什么是全局变量？
# A: 在外部定义，且在整个.py文件中生效的变量

# Q3:
# login() 函数内部生成 token 后，
# 为什么更推荐 return token，
# 而不是让其他函数直接读取 login() 里的 token？
# A:return token代表login()函数将token的内容作为返回值。其他函数拿到这个返回值之后可以进行赋值或其他操作。