api_result = {
    "status_code": 200,
    "business_code": 0,
    "response_time": 620,
    "token": "abc123",
    "data": {
        "user_id": 10001,
        "username": "test_user"
    },
    "error": None
}
# 要求先取出：
# status_code
# business_code
# response_time
# token
# data
# error
status_code = api_result["status_code"]
busiss_code = api_result["business_code"]
response_time = api_result["response_time"]
token = api_result["token"]
data = api_result["data"]
error = api_result["error"]
# 然后完成以下判断。
# 200 → HTTP请求成功
# 其他 → HTTP请求失败

if status_code == 200:
    print("HTTP请求成功")
else:
    print("HTTP请求失败")

# 业务码
# 只有在：
# status_code == 200
# 时，再判断：
# business_code == 0 → 业务处理成功
# 否则 → 业务处理失败

if status_code == 200:
    if busiss_code == 0:
        print("业务处理成功")

    else:
        print("业务处理失败")

# <= 300       → 响应速度优秀
# <= 500       → 响应速度正常
# <= 1000      → 响应速度较慢
# > 1000       → 响应速度异常
if response_time <= 300:
    print("响应速度优秀")
elif response_time <= 500:
    print("响应速度正常")
elif response_time <= 1000:
    print("响应速度较慢")
elif response_time > 1000:
    print("响应速度异常")

# 4. 如果：data有内容：返回数据不为空
# 否则：返回数据为空
if data:
    print("返回数据不为空")
else:
    print("返回数据为空")
# 5. Token
# 如果：token is not None
# 输出：Token存在
# 否则：Token缺失

if token is not None:
    print("Token存在")
else:
    print("Token缺失")

# 6. 最终通过条件
# 先创建：
# api_pass = ...
# 必须同时满足：
# status_code == 200
# business_code == 0
# response_time <= 1000
# token is not None
# data 非空
# error is None
#
# 然后：
# if api_pass:
#     print("接口测试结果：PASS")
# else:
#     print("接口测试结果：FAIL")
#
# 要求：
# 最终判断必须使用 api_pass 变量。
# 不要在 if 里重新写一遍全部条件。
# 不使用循环。
# 不使用函数。
api_pass = (status_code==200 and busiss_code==0 and
            response_time <= 1000 and token is not None
            and data and error is None)

if api_pass:
    print("接口测试结果:PASS")
else:
    print("接口测试结果:FAIL")
