print("——————————————————练习一：创建和读取字典————————————————————")
# 完成：
# 打印完整字典。
# 打印字典类型。
# 打印字典长度。
# 使用方括号读取 status_code。
# 使用方括号读取 message。
# 使用 get() 读取 token。
# 使用 get() 读取不存在的 user_id。
# 使用 get() 读取不存在的 environment，默认值设为 "test"。
# 判断 "token" 是否是字典的键。
# 判断 "user_id" 是否不是字典的键。
# 打印 error 是否为 None。
#
# 要求：不直接写死输出结果。
# 至少分别使用一次方括号和 get()。
# 不使用 if/else。
login_response = {
    "status_code": 200,
    "message": "login success",
    "token": "abc123",
    "response_time": 125.68,
    "passed": True,
    "error": None
}
print("打印完整字典:", login_response)
print(f"login_response的类型为:{type(login_response)}, 长度为:{len(login_response)}")
print(f"状态码为:{login_response['status_code']}")
print(f"信息:{login_response['message']}")
print(f"token:{login_response.get('token')}")
print(f"user_id:{login_response.get('user_id')}")
print(f"environment:{login_response.get('environment', 'test')}")
print(f"token是否是字典的键：{'token' in login_response}")
print(f"user_id是否不是字典的键：{'user_id' not in login_response}")
print(f"error是否尾None:{login_response['error'] is None}")

print("——————————————————练习二：键和值的判断————————————————————")
# 继续定义：
response_data = {
    "code": 200,
    "message": "success"
}
# 分别输出：
# "code" in response_data
# 200 in response_data
# "message" in response_data
# "success" in response_data
#
# 在注释中回答：
# Q 为什么 "code" in response_data 是 True？
# A 因为 in 只判断键是否存在，code正好是键

# Q 为什么 200 in response_data 是 False？
# A 因为 in 只判断键是否存在，200是值，所以不存在

# Q 字典直接使用 in 时，检查的是键还是值？
# A 检查的是键，不是值

print("code" in response_data)
print(200 in response_data)
print("message" in response_data)
print("success" in response_data)

