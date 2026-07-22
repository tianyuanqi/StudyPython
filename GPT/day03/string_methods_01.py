print("————————————————————分割线，用户输入清洗————————————————————")
# 用户从键盘输入任意内容，要求：假设用户输入  Admin_User
# 去除左右两侧空白。
# 将用户名转换为全小写。
# 打印原始输入内容。
# 打印清洗后的用户名。
# 判断清洗后的用户名是否以 "admin" 开头。
# 判断用户名中是否包含 "user"。ee
# 打印原始字符串和清洗后字符串的长度。
user_input = input("请输入任意内容")
clean_input = user_input.strip().lower()
print("原始输入内容为:", user_input)
print("清洗后的内容为:", clean_input)
print("是否以admin为开头:", clean_input.startswith("admin"))
print("是否包含user", "user" in clean_input)
print("原始字符串长度:", len(user_input))
print("清洗后的字符串长度:", len(clean_input))

print("————————————————————分割线，练习二：接口路径处理————————————————————")
# 定义：
# api_path = "/api/v1/user/login"
# 完成并打印：
# 判断路径是否以 "/api" 开头。
# 判断路径是否以 "login" 结尾。
# 查找 "user" 第一次出现的索引。
# 将 "v1" 替换为 "v2"。
# 将路径按照 "/" 拆分。
# 打印拆分结果的类型。
# 观察拆分结果的第一个元素是什么，并在注释中说明原因。
# 不能直接写出替换后的完整路径。观察拆分结果的第一个元素是什么，并在注释中说明原因。
api_path = "/api/v1/user/login"
print("判断路径是否以 '/api' 开头:", api_path.startswith("/api"))
print("判断路径是否以 'login 结尾':", api_path.endswith("login"))
print("查找 'user' 第一次出现的索引:", api_path.find("user"))
print("将v1替换为v2:", api_path.replace("v1", "v2"))
result = api_path.split("/")
print("路径按照/拆分:", result)
# 拆分后第一个元素是""，因为是按照"/"来拆分，字符串中间的/会直接去掉，开头和末尾如果有/，切掉之后会填充""进去
print("拆分后的数据类型:", type(result))

print("————————————————————分割线，练习三：测试数据拆分与重组————————————————————")

# 定义：
# case_data = "LOGIN_001_SUCCESS"
# 要求：
# 使用 split("_") 拆分字符串。
# 打印拆分结果。
# 通过索引读取拆分后的三个部分。
# 将三个部分全部转换为小写。
# 使用 "-".join(...) 重新连接，生成：
# login-001-success
# 判断中间部分是否全部为数字。
# 判断第一部分是否全部为字母。
#
# 不要直接把最终结果写死。

case_data = "LOGIN_001_SUCCESS"
result_data = case_data.split("_")
print("拆分后的结果为:", result_data)
print("读取拆分后的三个部分:", result_data[0], result_data[1], result_data[2])
result_data = [
    result_data[0].lower(),
    result_data[1].lower(),
    result_data[2].lower()
]
print("三个部分转小写以后:", result_data)
print("用-join()连接以后:", "-".join(result_data))

print("判断中间部分是否为数字:", result_data[1].isdigit())
print("判断第一部分是否为字母:", result_data[0].isalpha())

print("————————————————————分割线，练习四、变式挑战————————————————————")

# 定义：
# raw_log = "  ERROR|login failed|code=401  "
# 要求逐步处理：
# 去除两端空白。
# 将全部内容转换为小写。
# 将 "failed" 替换为 "failure"。
# 按照 "|" 拆分。
# 打印拆分后的三部分。
# 判断第一部分是否等于 "error"。
# 判断最后一部分是否以 "401" 结尾。
# 使用 " - " 将三部分重新连接。
#
# 本题不要把所有方法堆在一行中。每一步使用语义明确的变量保存结果，便于检查。
raw_log = "  ERROR|login failed|code=401  "

strip_raw_log = raw_log.strip()  # 去除两端空白
lower_raw_log = strip_raw_log.lower()  # 全部变为小写
replace_raw_log = lower_raw_log.replace("failed", "failure")
split_raw_log = replace_raw_log.split("|")
print("打印拆分后的三部分:", split_raw_log[0], split_raw_log[1], split_raw_log[2])
print("判断第一部分是否等于error:", split_raw_log[0] == "error")
print("判断最后一部分是否以401结尾", split_raw_log[2].endswith("401"))
join_raw_log = " - ".join(split_raw_log)
print("用-将三部分重新连接:", join_raw_log)
