# 分别定义4个函数
# 200 → True
# 其他 → False
def check_status(status_code):
    if status_code == 200:
        return True
    else:
        return False


def check_business(business_code):
    if business_code == 0:
        return True
    else:
        return False


def check_response_time(response_time):
    if response_time <= 1000:
        return True
    else:
        return False


def check_token(token):
    # if token != None and token != "":
    if token:
        return True
    else:
        return False


api_result = {
    "status_code": 200,
    "business_code": 0,
    "response_time": 650,
    "token": "abc123",
    "data": {
        "user_id": 10001,
        "username": "test_user"
    }
}

status_pass = check_status(api_result["status_code"])
business_pass = check_business(api_result["business_code"])
response_time_pass = check_response_time(api_result["response_time"])
token_pass = check_token(api_result["token"])

api_pass = (status_pass and business_pass and response_time_pass and token_pass)


if api_pass:
    print("接口测试结果:PASS")
else:
    print("接口测试结果:Fail")

print("——————————————————————————————分割线，以下是失败场景————————————————————————————————————")

failed_api_result = {
    "status_code": 200,
    "business_code": 1001,
    "response_time": 1500,
    "token": ""
}
status_pass = check_status(failed_api_result["status_code"])
business_pass = check_business(failed_api_result["business_code"])
response_time_pass = check_response_time(failed_api_result["response_time"])
token_pass = check_token(failed_api_result["token"])
api_pass = (status_pass and business_pass and response_time_pass and token_pass)

if api_pass:
    print("接口测试结果:PASS")
else:
    print("接口测试结果:Fail")