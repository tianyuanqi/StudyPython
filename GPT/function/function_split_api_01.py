api_response = {
    "status_code": 200,
    "json": {
        "business_code": 0,
        "token": "token_abc123",
        "user_id": 10001
    }
}


# 分别定义
# def check_status(response):
# 要求status_code == 200 → True  否则 → False

def check_status(response):
    if response["status_code"] == 200:
        return True
    else:
        return False

# 要求business==0  → True 否则 → False
def check_business(response):
    if response["json"]["business_code"] == 0:
        return True
    else:
        return False


def extract_login_data(response):
    token = response["json"]["token"]
    user_id = response["json"]["user_id"]
    return token, user_id



def api_pass(api_response):
    status_pass = check_status(api_response)
    business_pass = check_business(api_response)
    token, user_id = extract_login_data(api_response)

    api_pass = all([
        status_pass,
        business_pass,
        token,
        user_id
    ])
    if api_pass:
        print("登录接口检查通过")
    else:
        print("登录接口检查失败")
    return

api_pass(api_response)



print("————————————失败场景————————————")
failed_response = {
    "status_code": 200,
    "json": {
        "business_code": 1001,
        "token": "",
        "user_id": None
    }
}

api_pass(failed_response)
