class LoginRequest:

    def __init__(self, username, password):
        self.username = username
        self.password = password


class ApiResponse:

    def __init__(self, status_code, business_code, token):
        self.status_code = status_code
        self.business_code = business_code
        self.token = token


def login(request):
    if request.username == "test_user" and request.password == "123456":
        return ApiResponse(
            status_code=200,
            business_code=0,
            token="token_abc123"
        )
    else:
        return ApiResponse(
            status_code=200,
            business_code=1001,
            token=""
        )


def check_response(response):
    if response.status_code == 200 and response.business_code == 0 and bool(response.token):
        return True
    else:
        return False


success_request = LoginRequest(username="test_user", password="123456")
success_response = login(success_request)

if check_response(success_response):
    print("成功请求:PASS")
else:
    print("成功请求:FAIL")

fail_request = LoginRequest(username="test_user", password="wrong_password")
fail_response = login(fail_request)

if check_response(fail_response):
    print("失败请求:PASS")
else:
    print("失败请求:FAIL")

# Q1:
# login(request) 接收的 request 是什么类型？
# A:是LoginRequest类型

# Q2:
# login() 返回的是什么类型？
# A:返回的ApiResponse类型参数

# Q3:
# success_request 和 success_response
# 是不是同一个对象？
# A:不是同一个对象，success返回的是LoginRequest类型参数，success_response返回的是ApiResponse类型参数

# Q4:
# 本题的数据流可以怎样描述？
# A: 创建一个LoginRequest类型的对象，传入username和password两个参数，
# 然后把这个对象当做参数去调用login方法，返回一个ApiResponse类型的对象，这个对象记录的是返回值的相关信息，
# 最后把记录返回值的对象作为参数传入check_response方法去检查返回值是否符合要求

