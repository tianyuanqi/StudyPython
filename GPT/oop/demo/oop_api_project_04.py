from GPT.oop.demo.data_loader_04 import load_json
from GPT.oop.demo.login_api_04 import LoginApi


def run_testcases():
    login_api = LoginApi("www.test.com", timeout=5)

    testcases = load_json("login_cases_04.json")

    for testcase in testcases:
        response = login_api.login(
            username=testcase["username"],
            password=testcase["password"]
        )
        if (response.status_code == testcase["expected_status_code"]
                and response.business_code == testcase["expected_business_code"]):
            print(f"用户名:{testcase['case_name']}:PASS")
        else:
            print(f"用户名:{testcase['case_name']}:FAIL")


run_testcases()

# Q1:
# LoginApi 为什么可以调用 build_url()？
# A: 因为LoginApi是BaseApi的子类，子类对象继承了父类的方法


# Q2:
# login_api.login() 返回的是字典还是对象？
# 返回的具体是什么类型？
# A: 返回的是一个ApiResponse的对象


# Q3:
# response.data 是什么类型？
# 如果登录成功，怎样获取 token？
# A: 是字典类型，如果登录成功，可以使用response.data['token']去获取token

# Q4:
# data_loader_04.py 为什么没有必要
# 一定写成一个 class？
# A: 因为打开文件的操作基本都是一样的，没必要单独写成一个class


# Q5:
# wrong_password 接口返回 business_code=1001，
# 为什么测试用例仍然应该显示 PASS？
# A: 因为接口返回的business_code和测试用例里面定义的预期返回值一致，即可算该条用例通过


# Q6:
# 本项目完整的数据流是什么？
# 从 JSON 开始描述到 PASS / FAIL。
# A:
