print("错题1")
passed_cases = 18
total_cases = 20
# pass_rate = passed_cases / total_cases * 100 #不需要乘100，.2%会自动乘100，然后加上%
pass_rate = passed_cases / total_cases
# print(f"通过率：{pass_rate:.2%}%") #多打了一个百分比，.2%会自动加上%，所以不用另外手动加
print(f"通过率：{pass_rate:.2%}")

print("错题2")
response_times = [300, 100, 200]
sorted_times = response_times.sort()
# print(sorted_times[0]) # sort() 方法返回的是None，所以不能用[0]，所以运行会失败
print(response_times)

print("错题3")
cases = ["login", "register", "logout"]
reversed_cases = cases.reverse()
# print(reversed_cases[-1])  reverse() 返回None，所以会报错
# 需要同时打印：
# reverse() 返回值
# 真正被反转后的列表
print(reversed_cases)
print(cases)

print("错题4")
# 目标结果["login", "register", "logout"]
cases = ["login"]
# cases.append(["register", "logout"])
cases.extend(["register", "logout"])
print(cases)

print("错题5")
username = "  ADMIN  "
# username.strip() 不会修改原始字符串，所以错了
# username.lower() 不会修改原始字符串，所以错了
strip_username = username.strip()
lower_username = strip_username.lower()
print(lower_username)
# 目标输出admin

print("错题6")
status_codes = [200, 201, 404]
# print("201是否存在：", 200 in status_codes) 打错了
print("201是否存在：", 201 in status_codes)

print("错题7")
cases = ["login", "register", "logout"]
# first_case = cases[0:1]
# print(type(first_case))
# 原需求是取得字符串 "login"，说明应该怎样修改。
# first_case = cases.index(1)
print(type(cases[0]))  # 用索引直接找到第一个元素就好了

print("错题8")
numbers = [30, 10, 20]
numbers.reverse()
# print("降序排序结果：", numbers) 这里直接输出了反转结果，没有做降序排列
# 反转结果：[20, 10, 30]
# 降序排序结果：[30, 20, 10]
print("反转降序排序结果为:", sorted(numbers,reverse=True))
