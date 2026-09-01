
class ApiResponse:
    def __init__(
            self,
            status_code,
            business_code,
            token
    ):
        self.status_code = status_code
        self.business_code = business_code
        self.token = token

    def check_status(self):
        if self.status_code == 200:
            return True
        else:
            return False

    def check_business(self):
        if self.business_code == 0:
            return True
        else:
            return False

    def check_token(self):
        if self.token is not None:
            return True
        else:
            return False


def check_api(response):
    if response.check_status() and response.check_business and response.check_token:
        return True
    else:
        return False



success_response = ApiResponse(
    status_code=200,
    business_code=0,
    token="token_abc123"
)

failed_response = ApiResponse(
    status_code=500,
    business_code=1001,
    token=""
)

if(check_api(success_response)):
    print("成功响应:PASS")
else:
    print("成功响应:FAIL")

if(check_api(failed_response)):
    print("失败响应:PASS")
else:
    print("失败响应:FAIL")



# Q1:
# ApiResponse 类为什么可以创建
# success_response 和 failed_response 两个不同对象？
# A: 每初始化一次，都可以产生一个独立的对象，
# response作为返回值的类，只需要在初始化时传入不同的参数即可生成正确的返回对象以及失败的返回对象

# Q2:
# success_response.status_code
# 和
# failed_response.status_code
# 为什么可以保存不同的数据？
# A: 因为它们都属于不同的对象（实例），每个对象会保存一个状态码

# Q3:
# 把 status_code / business_code / token
# 和它们对应的检查方法放到同一个类中，
# 有什么好处？
# A: 在有很多对象需要判断时，不用写重复的代码，直接调用类函数（方法）就好了