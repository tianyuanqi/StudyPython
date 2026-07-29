status_code = 200
has_token = True
error_message = None
response_time = 850
environment = "test"

# 分别把以下判断保存到变量：
# 状态码为 200
# 存在 Token
# 错误信息为 None
# 响应时间不超过 1000 毫秒
# 环境是 test 或 staging
# 环境不是 production
status_code_pass = status_code == 200
token_pass = has_token
error_message_pass = error_message is None
response_time_pass = response_time <= 1000
environment_pass = environment in ["test", "staging"]
environment_not_production = environment != "production"

api_pass = (status_code_pass and token_pass and error_message_pass and
            environment_pass and response_time_pass and environment_not_production)
# 然后组合为最终变量：
#
# api_pass = ...
#
# 最终通过必须同时满足全部条件，特别注意不能遗漏：
#
# error_message is None
#
# 输出格式：
#
# 状态码正确：True
# Token存在：True
# 没有错误：True
# 响应时间合格：True
# 环境允许：True
# 不是生产环境：True
# 接口整体通过：True
#
# 要求：
# 每项条件先保存到变量。
# 最终条件使用前面保存的变量组合。
# 不使用 if/else。
# 不直接写死 True。

print(f"状态码正确:{status_code_pass}")
print(f"Token存在:{token_pass}")
print(f"没有错误:{error_message_pass}")
print(f"响应时间合格:{response_time_pass}")
print(f"环境允许:{environment_pass}")
print(f"不是生产环境:{environment_not_production}")
print(f"接口整体通过:{api_pass}")
