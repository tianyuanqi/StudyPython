from pprint import pprint

test = "hello_world"
print(test[3])  # 索引从0开始，取下标为3的元素，也就是第4个,实际打印l
print(test[2:5])  # 索引从2开始，一直取到下标为4的元素（包含左边，不包含右边），实际打印llo
print(test[-5])  # 从右往左开始，右边第一个为-1，打印下标为-5的元素，实际打印w
print(test[::2])  # 开始位置:结束位置:步长，不写表示从都到尾，2表示每次步长为2，也就是跳过一个元素
pprint(test[::-1])  # 开始位置:结束位置:步长，不写表示从都到位，步长为负数表示从右到左反过来提取

print("———————————————分割线练习一：接口名称拆解————————————————————")
# 定义api_name = "user_login"
# 要求打印
# 第一个字符。
# 最后一个字符。
# 字符串长度。
# 索引 5 对应的字符。
# 使用负索引读取倒数第二个字符。
# 使用 len() 计算最后一个字符的正向索引。

api_name = "user_login"
print("第一个字符为:", api_name[0])
print("最后一个字符为:", api_name[-1])
print("字符串长度为:", len(api_name))
print("索引 5 对应的字符:", api_name[5])
print("使用负索引读取倒数第二个字符:", api_name[-2])
print("使用 len() 计算最后一个字符的正向索引:", len(api_name) - 1)

print("————————————————————分割线，练习二————————————————————")

# 练习二：定义：case_id = "LOGIN_001_SUCCESS"
# 使用切片分别得到并打印：
# LOGIN
# 001
# SUCCESS
#
# 要求：
# 不能直接把三个结果写死。
# 必须从 case_id 中切片得到。
# 至少使用一次省略开始位置的切片。
# 至少使用一次省略结束位置的切片。
#
# 再打印：
# case_id 的前五个字符。
# case_id 的最后七个字符。
# 完整字符串的倒序结果。
case_id = "LOGIN_001_SUCCESS"
print("打印Login:", case_id[:5])
print("打印001:", case_id[6:9])
print("打印SUCCESS:", case_id[10:])

print("前5个字符", case_id[:5])
print("最后七个字符:", case_id[-7:])
print("完整字符串的倒序结果:", case_id[::-1])

print("————————————————————分割线，练习三————————————————————")
phone_number = "13812345678"
# 通过索引、切片和字符串拼接，生成：
# 138****5678
# 要求：
# 前三位必须从原字符串中截取。
# 后四位必须从原字符串中截取。
# 中间的 "****" 可以直接写。
# 原手机号不能直接写进结果字符串。
# 打印原手机号长度。
# 判断原手机号长度是否等于 11，打印布尔结果。
# 暂时不使用 if/else。

first_phone_number = phone_number[0:3]
last_phone_number = phone_number[-4:]
Encrypted_phone_number = first_phone_number + "****" + last_phone_number
print("加密后的手机号为:", Encrypted_phone_number)
print("原手机号的长度为:", len(phone_number))
print("判断原手机号长度是否等于11:", len(phone_number) == 11)


