# 定义登录函数
# 要求：如果
# username == "test_user"
# and password == "123456"
# 返回："login_success"，否则返回 "login_failed"


def login(username, password):
    if username == "test_user" and password == "123456":
        return "login_success"
    else:
        return "login_failed"


test_cases = [{"username": "test_user", "password": "123456"},
              {"username": "test_user", "password": "wrong_password"}]
# index = 0
# for i in test_cases:
#     result = login(test_cases[index].get("username"), test_cases[index].get("password"))
#     if result == "login_success":
#         print(f"第{index+1}次登录成功")
#         index += 1
#     else:
#         print(f"第{index+1}次登录失败")
#         index += 1


for index, i in enumerate(test_cases, start=1):
    result = login(i.get("username"), i.get("password"))
    if result == "login_success":
        print(f"第{index}次登录成功")
    else:
        print(f"第{index}次登录失败")

print("————————————————————分割线————————————————————")


# 规则：<= 500     → 返回 "normal"
# 501~1000   → 返回 "slow"
# > 1000     → 返回 "timeout"

# check_response_time(300)
# check_response_time(800)
# check_response_time(1500)
# 把三个返回值保存到三个变量中，再打印。
# normal
# slow
# timeout

def check_response_time(response_time):
    if response_time <= 500:
        return "normal"
    elif response_time <= 1000:
        return "slow"
    elif response_time > 1000:
        return "timeout"


first = check_response_time(300)
second = check_response_time(800)
third = check_response_time(1500)
print(first)
print(second)
print(third)
