numbers = [
    1, 2, 3, 4, 5, 6
]

# 使用列表推导式生成一个event_numbers,只保存原列表的偶数部分（2,4,6）
event_numbers = [
    i
    for i in numbers
    if i % 2 == 0
]
print(event_numbers)

# 再使用列表推导式将原列表乘2
double_numbers = [
    number * 2
    for number in numbers
]
print(double_numbers)

# 定义
cases = [
    {
        "case_name": "login_success",
        "enabled": True
    },
    {
        "case_name": "wrong_password",
        "enabled": False
    },
    {
        "case_name": "wrong_username",
        "enabled": True
    }
]

# 使用列表推导式生成enabled_cases，要求只保留 enable == True
enable_cases = [
    case
    for case in cases
    if case["enabled"] == True
]

print(enable_cases)

# 再使用列表推导式生成enabled_case_names
# 要求最终
# [
#     "login_success",
#     "wrong_username"
# ]

enable_case_names = [
    case['case_name']
    for case in cases
    if case["enabled"] == True
]
print(enable_case_names)

# Q1:
# 列表推导式主要适合做什么？
# A: 适合根据一个可迭代的列表，快速生成一个新的列表


# Q2:
# 下面两部分分别负责什么？
#
# case["case_name"]
# for case in cases
#
# A: for case in cases表示遍历原始的cases数组，case["case_name"]表示把每个元素的case_name单独取出来


# Q3:
# 如果推导式中的判断和处理逻辑非常复杂，
# 是否还应该强行写成一行？
# A: 不应该写成一行，需要保证代码的可读性，如果逻辑过于复杂甚至不建议使用推导式
