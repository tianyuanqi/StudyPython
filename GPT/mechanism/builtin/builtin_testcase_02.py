testcases = [
    {
        "case_name": "wrong_password",
        "priority": 3,
        "enabled": True,
        "status_code": 200,
        "expected_status_code": 200
    },
    {
        "case_name": "disabled_case",
        "priority": 1,
        "enabled": False,
        "status_code": 500,
        "expected_status_code": 200
    },
    {
        "case_name": "login_success",
        "priority": 1,
        "enabled": True,
        "status_code": 200,
        "expected_status_code": 200
    },
    {
        "case_name": "server_error",
        "priority": 2,
        "enabled": True,
        "status_code": 500,
        "expected_status_code": 200
    }
]

# 用列表推导式只保留enabled == True，得到enabled_cases
enabled_cases = [
    case
    for case in testcases
    if case["enabled"] == True
]
print(enabled_cases)

# 用sorted()按priority从小到大排序
sort_cases = sorted(enabled_cases, key=lambda case: case["priority"])
print(sort_cases)

# 使用enumerate(..., start=1)逐条打印：
# 第1条:login_success
# 第2条:server_error
# 第3条:wrong_password
# 注意：login_success 和其他 case 的相对顺序要以 sorted() 的实际稳定排序结果为准；
# 重点是 disabled_case 不参与执行，并且 priority 从小到大。

for index, case in enumerate(sort_cases, start=1):
    print(f"第{index}条:", case['case_name'])

# 第四步，为每条启用用例生成检查结果：
status_pass = (
    case["status_code"]
    == case["expected_status_code"]
    for case in  sort_cases
)
# 把这些结果保存到：check_results，
# 最终结果应该类似[
#     True,
#     False,
#     True
# ]
# 然后分别
# print(all(check_results))
# print(any(check_results))
check_results=[i for i in status_pass]

print(all(check_results))
print(any(check_results))

# Q1:
# 为什么 disabled_case 没有进入后面的执行流程？
# A: 因为disabled_case代表测试用例的状态，启用或者未启用，通过该状态去判断需要执行的用例，该字段本身不应该被加入执行流程


# Q2:
# all(check_results) 为什么是 False？
# A: 因为check_results中只要有一个False，call(check_results)就会返回False


# Q3:
# any(check_results) 为什么是 True？
# A: 因为check_results中只要有一个True，any(check_results)就会返回True


# Q4:
# 本题的数据处理流程是什么？
# 从原始testcases开始描述。
# A: