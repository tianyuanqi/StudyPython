# 规则
# 用户名 = test_user
# 密码 = 123456
# 则return "token_abc123"，否则return None

def login(username, password, timeout=5):
    if username == "test_user" and password == "123456":
        return "token_abc123"
    else:
        return None


print("————————————————————分割线————————————————————")


def get_user_info(token, timeout=5):
    if token:
        return {
            "user_id": 10001,
            "username": "test_user"
        }

    else:
        return None


token = login("test_user", "123456")

user_info = get_user_info(token, 10)

if token and user_info:
    print("接口流程执行成功")
else:
    print("接口流程执行失败")

print("————————————————————分割线，失败场景————————————————————")
faild_token = login("test_user", "wrong_password")

faild_user_info = get_user_info(token=faild_token, timeout=10)
if faild_token and faild_user_info:
    print("接口流程执行成功")
else:
    print("接口流程执行失败")
