print("——————————————————————————————复习题一：格式化测试结果——————————————————————————————")

# 定义：
case_number = 8
api_name = "user_login"
status_code = 200
response_time = 126.578
passed_cases = 18
total_cases = 20

# 计算通过率，并使用一个 f-string 输出：
# CASE_008 | user_login   | 200 | 126.58 ms | 通过率：90.00%
# 要求：
# 用例编号三位补零。
# 接口名称占 12 个字符宽度，左对齐。
# 响应时间保留两位小数。
# 通过率不能提前乘以 100。
# 整行使用一个 f-string。

passed_percent = passed_cases / total_cases
print(f"CASE_{case_number:03d} | {api_name:<12} | {status_code} | {response_time:.2f} ms | {passed_percent:.2%}")

print("——————————————————————————————复习题二：列表增删操作——————————————————————————————")

# 定义：
test_cases = ["login", "register", "logout"]
# 依次完成：
# 将 "register" 修改为 "user_register"。
# 末尾添加 "profile"。
# 开头插入 "health_check"。
# 批量添加：
# ["update_user", "delete_user"]
# 删除 "logout"。
# 使用不带参数的 pop() 删除最后一个元素，并保存返回值。
# 打印最终列表、删除的元素和列表长度。

test_cases[1] = "user_register"
test_cases.append("profile")
test_cases.insert(0, "health_check")
test_cases.extend(["update_user", "delete_user"])
test_cases.remove("logout")
end_data = test_cases.pop()
print("最终的列表为:",test_cases,"被pop删除的元素为:",end_data,"最终长度为:",len(test_cases))
