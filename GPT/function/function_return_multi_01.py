

# 成功时返回  return "token_abc123", 10001
# 失败时返回 return None, None
def login(username, password):
    if username == "test_user" and password == "123456":
        token="token_abc123"
        code=10001
        return token,code
    else:
        return None,None

# 调用成功场景
token, user_id = login(
    username="test_user",
    password="123456"
)
print(f"token:{token}")
print(f"user_id:{user_id}")

# 调用失败场景
failed_token, failed_user_id = login(
    username="test_user",
    password="wrong"
)
if not failed_token and failed_user_id is None:
    print("登录失败")

# Q1:
# Python函数 return a, b 时，
# 实际返回的数据类型通常是什么？
# A:本质上是返回了一个元组

# Q2:
# token, user_id = login()
# 这种写法叫什么？
# A:多个返回值拆包，本质上是把返回的元组，按位置顺序拆分赋值给对应的变量