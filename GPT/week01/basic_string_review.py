print("————————————————————练习二：基础数据和布尔判断——————————————————————————————")
status_code = 200
has_token = True
error_message = None
response_time = 850
environment = "test"

# 分别创建变量，完成以下判断：
# 状态码是否为 200。
# 是否存在 Token。
# 错误信息是否为 None。
# 响应时间是否不超过 1000 毫秒。
# 环境是否为 "test" 或 "staging"。
# 环境是否不是 "production"。
# 接口是否满足以下全部条件：

print(f"状态码为200:{status_code == 200}")
print(f"是否存在token:{has_token}")

print(f"没有错误信息,", error_message is None)

response_time_pass = response_time < 1000
print(f"响应时间合格:", response_time_pass)

environment_pass = environment in ["test", "staging"]
print(f"环境允许:{environment_pass}")
print(f"环境是否不是production:{environment != 'production'}")
api_pass = status_code == 200 and has_token and response_time_pass and environment_pass and environment != "production"
print(f"接口是否满足以下所有条件：{api_pass}")

print("————————————————————练习二：接口路径处理——————————————————————————")
raw_path = "  /API/V1/USER/LOGIN  "
# 依次完成：
#
# 去除两端空白。
# 全部转为小写。
# 判断是否以 /api 开头。
# 判断是否以 login 结尾。
# 查找 "user" 第一次出现的位置。
# 将 "login" 替换为 "signin"。
# 使用 / 拆分替换后的路径。
# 打印拆分结果的类型。
# 使用 " -> " 重新连接拆分结果。
# 确认原始字符串 raw_path 是否改变

strip_raw_path = raw_path.strip()
print("去除两端空白以后:", strip_raw_path)

low_raw_path = strip_raw_path.lower()
print("转小写以后:", low_raw_path)

start_with_path = low_raw_path.startswith("/api")
print("是否以/api开头:", start_with_path)

end_with_path = low_raw_path.endswith("login")
print("是否以login结尾:", end_with_path)

replace_path = low_raw_path.replace("login", "signin")
print("替换成sigin以后:", replace_path)

split_path = replace_path.split("/")
print(type(split_path))

join_path = "->".join(split_path)
print("原始字符串是否改变:", raw_path != "  /API/V1/USER/LOGIN  ")

print("————————————————————练习三：日志内容处理——————————————————————————")
raw_log = "  ERROR|user login failed|code=401  "
# 去除空白。
# 转为小写。
# 将 "failed" 替换为 "failure"。
# 使用 | 拆分。
# 判断第一部分是否为纯字母。
# 判断第三部分是否以 "401" 结尾。
# 使用 " - " 重新连接。
# 打印原日志和最终日志。
# 打印原日志长度和清洗后日志长度。
# 判断最终日志中是否包含 "failure"。

strip_raw_log = raw_log.strip()
print("去除空白以后:", strip_raw_log)

lower_log = strip_raw_log.lower()
print("转小写以后:", lower_log)

replace_log = lower_log.replace("failed", "failure")
print("替换以后:", replace_log)

split_log = replace_log.split("|")
print("拆分以后:", split_log)

print("第三部分是否以401结尾", split_log[2].endswith("401"))

join_log = "-".join(split_log)

print("原始日志为:", raw_log, " 原始日志长度为:", len(raw_log))
print("最终日志为:", join_log, " 最终日志长度为:", len(join_log))

print("————————————————————练习四：字符串格式化——————————————————————————————")
case_number = 12
api_name = "user_login"
status_code = 200
response_time = 137.568
passed_cases = 47
total_cases = 50

# 先计算通过率，再使用一个 f-string 输出：
#
# CASE_012 | user_login   | 200 | 137.57 ms | 通过率：94.00%
# 要求：
# 编号三位补零。
# 接口名称占 12 个字符宽度并左对齐。
# 响应时间保留两位小数。
# 通过率变量应处于 0～1。
# 不手动重复添加百分号。
# 整行使用一个 f-string。
pass_percent = passed_cases / total_cases
print(f"CASE_{case_number:03d} | {api_name:<12} | {status_code} | {response_time:.2f}ms | 通过率:{pass_percent:.2%}")