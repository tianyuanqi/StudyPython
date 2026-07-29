api_result = {
    "case_number": 7,
    "case_name": "user_login",
    "method": "POST",
    "path": "/api/v1/user/login",
    "status_code": 200,
    "response_time": 132.567,
    "token": "abc123",
    "error": None
}
# 将以下值分别保存到变量：
# 要求：
#     至少四个字段使用方括号读取。
#     至少两个字段使用 get() 读取。
#     使用 get() 读取不存在的 "environment"，默认值为 "test"。
case_number = api_result["case_number"]
case_name = api_result["case_name"]
method = api_result["method"]
path = api_result["path"]
status_code = api_result.get("status_code")
response_time = api_result.get("response_time")
token = api_result.get("token")
error = api_result.get("error")
enviroment = api_result.get("environment", "test")

print("——————————————第二部分：计算判断结果————————————————————")

status_pass = status_code == 200
response_time_pass = response_time <= 500
token_pass = token != None
error_pass = error is None
method_pass = method == "POST"
path_pass = path.startswith("/api")
api_pass = status_pass and response_time_pass and token_pass and error_pass and method_pass and path_pass

print("——————————————————第三部分：修改报告数据————————————————")
# 依次完成：
#     添加 "environment": "test"。
#     添加 "passed": api_pass。
#     将 "case_name" 修改为 "user_login_success"。
api_result.update({
    "environment": "test",
    "passed": api_pass,
    "case_name": "user_login_success"
})

#     使用 pop("token") 删除 Token，并保存返回值。
pop_token = api_result.pop("token")
#     打印删除 Token 后 "token" in api_result 的结果。
print(token in api_result)

#     使用 get("token", "Token已删除") 再次读取 Token。
print(api_result.get("token", "token已删除"))

print("————————————————————第四部分：输出报告——————————————————————")

print("================ 接口测试报告 ================")
print(f"CASE_{case_number:03d} | {case_name}")
print(f"请求方式:{method}")
print(f"接口路径:{path}")
print(f"运行环境:{enviroment}")
print(f"状态码:{status_code}")
print(f"响应时间:{response_time}")
print(f"状态码合格:{status_pass}")
print(f"响应时间合格:{response_time_pass} ms")
print(f"token合格:{token_pass}")
print(f"无错误信息:{error_pass}")
print(f"请求方式合格:{method_pass}")
print(f"接口路径合格:{path_pass}")
print(f"接口整体通过:{api_pass}", )
print(f"被删除的token:{pop_token}")
print(f"当前token:{api_result.get('token', 'token已被删除')}")
print(f"字典字段数量:", len(api_result))

print("==============================================")
