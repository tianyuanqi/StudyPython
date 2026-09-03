from data_loader_04 import load_json
from login_api_04 import LoginApi


def run_testcases():
    login_api = LoginApi(base_url="http://api.test.com", timeout=10)

    testcases = load_json("login_cases_04.json")

    for testcase in testcases:
        response = login_api.login(
            username=testcase["username"],
            password=testcase["password"]
        )
        print(f"接口业务是否成功:{response.is_success()}")
        if (response.status_code == testcase["expected_status_code"]
                and response.business_code == testcase["expected_business_code"]):
            print(f"测试用例执行结果:用户名:{testcase['case_name']}:PASS")
        else:
            print(f"测试用例执行结果:用户名:{testcase['case_name']}:FAIL")


if __name__ == "__main__":
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
# A: 因为load_json只是一个读取json文件的函数，没有需要长期保存到对象中的状态，所以用普通的函数即可，没必要定义成class


# Q5:
# wrong_password 接口返回 business_code=1001，
# 为什么测试用例仍然应该显示 PASS？
# A: 因为接口返回的business_code和测试用例里面定义的预期返回值一致，即可算该条用例通过


# Q6:
# 本项目完整的数据流是什么？
# 从 JSON 开始描述到 PASS / FAIL。
# A: 通过load_json方法读取文件，将测试数据保存到列表中，
# 然后通过循环遍历读取每条测试数据，
# 将username和password传入login()方法，然后拿到返回值（返回值是ApiResponse类的对象），
# 然后用返回值去调用is_success方法判断接口业务是否成功。
# 再接着取出返回值的status_code和business_code，去和测试数据中定义的预期值进行对比，
# 如果和预期值相同，则说明测试用例通过
