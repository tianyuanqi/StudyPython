import requests
import pytest

# 1. 准备测试数据
test_cases = [
    {"username": "admin", "password": "123456", "expected_code": 200},
    {"username": "test_user", "password": "wrongpwd", "expected_code": 401},
    {"username": "empty_user", "password": "", "expected_code": 400}
]

# 2. 核心请求逻辑 (不再需要 test_ 前缀，它只是个普通工具)
def send_login_request(username, password):
    url = "https://httpbin.org/post"
    userdata = {
        "username": username,
        "password": password
    }
    req = requests.post(url, json=userdata)
    return req.status_code

# 3. Pytest 真正的测试用例！
@pytest.mark.parametrize("case_data", test_cases)
def test_login_api(case_data):
    username = case_data["username"]
    password = case_data["password"]
    expected_code = case_data["expected_code"]

    actual_code = send_login_request(username, password)

    # 直接断言，不需要 try...except！
    assert actual_code == expected_code, f"账号 {username} 测试失败，预期:{expected_code}，实际:{actual_code}"