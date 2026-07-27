# 场景
# 某次接口测试得到以下原始数据：
# raw_case_name = "  USER_LOGIN  "
# raw_api_path = "  /API/V1/USER/LOGIN  "
#
# status_codes = [200, 200, 401, 200, 500]
# response_times = [125.5, 320.8, 98.2, 210.4, 150.0]
# test_results = [
#     "login_success",
#     "profile_success",
#     "token_failed",
#     "logout_success",
#     "server_failed"
# ]
# 第一部分：处理字符串
# 完成：
# 将用例名称清洗并转为小写。
# 将接口路径清洗并转为小写。
# 判断路径是否以 /api 开头。
# 判断路径是否以 login 结尾。
# 将路径按 / 拆分。
# 使用 " -> " 重新连接路径。
# 将所有 "failed" 替换为 "failure"，只处理指定字符串：
result_text = "token_failed|server_failed"
#
# 再使用 " | " 重新连接处理结果。

raw_case_name = "  USER_LOGIN  "
raw_api_path = "  /API/V1/USER/LOGIN  "

status_codes = [200, 200, 401, 200, 500]
response_times = [125.5, 320.8, 98.2, 210.4, 150.0]
test_results = [
    "login_success",
    "profile_success",
    "token_failed",
    "logout_success",
    "server_failed"
]
lower_case_name = raw_case_name.strip().lower()
lower_api_path = raw_api_path.strip().lower()
print(f"路径是否以/api开头:{lower_api_path.startswith('/api')}")
print(f"路径是否以/end开头:{lower_api_path.endswith('/login')}")
split_path = lower_api_path.split("/")
join_path = "->".join(split_path)

failure_text = result_text.replace("failed", "failure")
failure_parts = failure_text.split("|")
formatted_failure_text = " | ".join(failure_parts)
print("处理后的result_text:",formatted_failure_text)

# 第二部分：处理列表
#
# 完成：
#
# 状态码总数量。
# 200 的数量。
# 401 的数量。
# 500 的数量。
# 200 第一次出现的位置。
# 响应时间升序新列表。
# 最快、最慢、平均响应时间。
# 删除 test_results 中的 "profile_success"。
# 使用 pop() 删除最后一个测试结果并保存。
# 在列表开头插入 "prepare_success"。
# 在末尾批量增加：
# ["cleanup_success", "report_success"]
raw_case_name = "  USER_LOGIN  "
raw_api_path = "  /API/V1/USER/LOGIN  "

status_codes = [200, 200, 401, 200, 500]
response_times = [125.5, 320.8, 98.2, 210.4, 150.0]
test_results = [
    "login_success",
    "profile_success",
    "token_failed",
    "logout_success",
    "server_failed"
]
print(f"状态码总量:{len(status_codes)}")
print(f"200的数量:{status_codes.count(200)}")
print(f"401的数量:{status_codes.count(401)}")
print(f"500的数量:{status_codes.count(500)}")
print(f"200第一次出现的位置:{status_codes.index(200)}")
sorted_times = sorted(response_times)
print("响应时间升序新列表:", sorted_times)
print(
    f"最快响应时间:{min(response_times)}ms |"
    f" 最慢响应时间:{max(response_times)}ms | 平均响应时间:{sum(response_times) / len(response_times)}")
test_results.remove("profile_success")

pop_last = test_results.pop()
test_results.insert(0, "prepare_success")
test_results.extend(["cleanup_success", "report_success"])
print(test_results)

print("——————————————————————第三部分：计算测试结果————————————————————")
# 计算：
# 总用例数
# 成功状态码数量
# 状态码成功率(状态码200的数量 / 状态码总数量)
# 平均响应时间
# 路径是否合法(以 /api 开头,并且以 login 结尾)
raw_case_name = "  USER_LOGIN  "
raw_api_path = "  /API/V1/USER/LOGIN  "
status_codes = [200, 200, 401, 200, 500]
response_times = [125.5, 320.8, 98.2, 210.4, 150.0]
test_results = [
    "login_success",
    "profile_success",
    "token_failed",
    "logout_success",
    "server_failed"
]
print(f"总用例数:{len(status_codes)}:")
print(f"成功状态码数量：:{status_codes.count(200)}")
print(f"状态码成功率:{status_codes.count(200) / len(status_codes):.2%}")
print(f"平均响应时间:{sum(response_times) / len(response_times):.2f}ms")
lower_api_path = raw_api_path.strip().lower()
print(lower_api_path)
print(f"路径是否合法:{lower_api_path.startswith('/api') and lower_api_path.endswith('/login')}")

print("——————————————————第四部分：输出报告——————————————————————")
#
# 使用 f-string 输出：
#
# ================ 接口测试报告 ================
# 用例名称：user_login
# 接口路径：/api/v1/user/login
# 路径展示： -> api -> v1 -> user -> login
# 路径合法：True
# 总用例数：5
# 成功数量：3
# 成功率：60.00%
# 最快响应：98.20 ms
# 最慢响应：320.80 ms
# 平均响应：180.98 ms
# 响应时间升序：[98.2, 125.5, 150.0, 210.4, 320.8]
# 处理后的结果列表：实际计算结果
# 被 pop 删除的结果：实际删除结果
# 错误文本：token_failure | server_failure
# ==============================================
#

raw_case_name = "  USER_LOGIN  "
raw_api_path = "  /API/V1/USER/LOGIN  "
status_codes = [200, 200, 401, 200, 500]
response_times = [125.5, 320.8, 98.2, 210.4, 150.0]
test_results = [
    "login_success",
    "profile_success",
    "token_failed",
    "logout_success",
    "server_failed"
]
print("================ 接口测试报告 ================")
lower_case_name = raw_case_name.strip().lower()
print(f"用例名称:{lower_case_name}")
lower_api_path = raw_api_path.strip().lower()
print(f"接口路径:{lower_api_path}")
join_path = " -> ".join(lower_api_path.split("/"))
print(f"路径展示", join_path)
print(f"路径合法:{lower_api_path.startswith('/api') and lower_api_path.endswith('/login')}")
print(f"总用例数:{len(status_codes)}")
print(f"成功数量:{status_codes.count(200)}")
print(f"成功率:{status_codes.count(200) / len(status_codes):.2%}")
print(f"最快响应:{min(response_times):.2f}ms")
print(f"最慢响应:{max(response_times):.2f}ms")
print(f"平均响应:{sum(response_times) / len(response_times):.2f}ms")
sorted_response_times = sorted(response_times)
print(f"响应时间升序为:{sorted_response_times}")
# 处理后的结果列表：实际计算结果
print(f"被处理后的结果列表:{test_results}")
# 被 pop 删除的结果：实际删除结果
print(f"被pop删除的结果:{pop_last}")
# 错误文本：token_failure | server_failure
print(f"错误文本:{formatted_failure_text}")

print("==============================================")
# 要求：
#
# 所有结果通过变量计算。
# 不直接写死统计值。
# 不使用循环。
# 不使用 if/else。
# 原始 response_times 不能被修改。
# 百分比不能重复乘以 100。
# 不把 sort()、reverse() 的返回值当列表使用。
