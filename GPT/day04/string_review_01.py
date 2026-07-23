print("——————————————————————————复习题 1：清洗并拆分接口结果——————————————————————————————————-")
# 定义：
# raw_result = "  LOGIN_001_SUCCESS  "
# 要求：
# 去除两端空白。
# 转换为小写。
# 使用 _ 拆分。
# 判断中间部分是否全部为数字。
# 使用 " - " 重新连接。
# 打印原字符串和最终结果。
#
# 限制：
# 每一步使用不同变量保存。
# 不把最终结果直接写死。
# 不使用 if/else。
raw_result = "  LOGIN_001_SUCCESS  "
strip_result = raw_result.strip() #去除空格
print(strip_result)
lower_result = strip_result.lower() #转小写
print(lower_result)
split_result = lower_result.split("_") #根据_切分
print(split_result)
print("切分以后中间是否都是数字:", split_result[1].isdigit())
join_result = "-".join(split_result)
print("原字符串:",raw_result)
print("处理后的字符串:",join_result)


print("——————————————————————————复习题 2：日志内容判断——————————————————————————————————-")
# 定义：log_text = "ERROR|login failed|code=401"
# 打印以下判断结果：
# 是否以 "ERROR" 开头。
# 是否以 "401" 结尾。
# "failed" 第一次出现的位置。
# 是否包含 "login"。
# 把 "failed" 替换为 "failure"，并确认原字符串是否发生变化。
log_text = "ERROR|login failed|code=401"
print("是否以Error为开头:",log_text.startswith("ERROR"))
print("是否以401为结尾:",log_text.endswith("401"))
print("failed第一次出现的位置是:",log_text.find("failed"))
print("是否包含login:","login" in log_text)
print("把failed替换为failure:",log_text.replace("failed","failure"))