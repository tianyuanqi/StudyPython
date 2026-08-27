import json


def login(username, password):
    if username == "test_user" and password == "123456":
        return "success"

    return "failed"


with open("login_cases.json.py", "r", encoding="utf-8") as file:
    test_cases = json.load(file)
    print(test_cases)

    for index, test_case in enumerate(test_cases, start=1):
        actual = login(test_case["username"], test_case["password"])
        if actual == test_case["expected"]:
            print(f"第{index}条:PASS")
        else:
            print(f"第{index}条:FAIL")
# Q1:
# 为什么 login_cases.json 最外层使用 []？
# A: 因为是一个列表，列表的每一个元素都是一个字典，一个元素就是一条测试数据

# Q2:
# json.load() 后，每一条 case 通常是什么类型？
# A: 通常是字典类型

# Q3:
# 接口登录失败，为什么对应的测试用例仍然可能 PASS？
# A: 因为有些测试数据的预期结果就是失败，只要和预期结果相等就可以PASS