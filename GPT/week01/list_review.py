print("————————————————————————练习一：列表索引和切片——————————————————————————")
test_cases = [
    "prepare_data",
    "user_login",
    "create_order",
    "pay_order",
    "user_logout"
]
# 打印：
# 完整列表。
# 列表类型。
# 列表长度。
# 第一个元素。
# 最后一个元素。
# 中间三个元素。
# 最后两个元素。
# 倒序新列表。
# test_cases[1] 的类型。
# test_cases[1:2] 的类型。
# "pay_order" 是否存在。
# "delete_order" 是否不存在。
print("打印完整列表:", test_cases)
print("列表类型:", type(test_cases))
print("列表长度:", len(test_cases))
print("第一个元素:", test_cases[0])
print(f"最后一个元素:{test_cases[-1]}")
print(int(len(test_cases) / 2) + 1)
print(f"中间三个元素:{test_cases[int(len(test_cases) / 2 - 1):int(len(test_cases) / 2 + 2)]}")
print(f"最后两个元素:{test_cases[-2:]}")
print(f"倒序新表为:", test_cases[::-1])
print(f"test_case[1]的类型:", type(test_cases[1]))
print(f"test_case[1:2]的类型:", type(test_cases[1:2]))
print(f"pay_order是否存在:{'pay_order' in test_cases}")
print(f"delete_order是否不存在:{'delete_order' not in test_cases}")

print("————————————————————————练习二：修改和增删——————————————————————————")
# 定义：
test_cases = ["login", "register", "logout"]
# 依次完成：
# 将 "login" 修改为 "user_login"。
# 将 "register" 修改为 "user_register"。
# 末尾添加 "profile"。
# 在开头插入 "health_check"。
# 批量添加：
# ["update_user", "delete_user"]
# 删除 "logout"。
# 使用无参数 pop() 删除最后一个元素，并保存返回值。
# 使用 pop(1) 删除索引 1 的元素，并保存返回值。
# 打印最终列表。
# 打印两次 pop() 删除的元素。
# 打印最终长度。
# 每完成一次修改，都打印当前列表。

test_cases[0] = "user_login"
print(f"修改login以后:{test_cases}")
test_cases[1] = "user_register"
print(f"修改register以后:{test_cases}")
test_cases.append("profile")
print(f"末尾添加profile以后{test_cases}")
test_cases.insert(0, "health_check")
print(f"在开头插入heal_check以后:{test_cases}")
test_cases.extend(["update_user", "delete_user"])
print(f"批量添加以后:{test_cases}")
test_cases.remove("logout")
print(f"删除logout以后:{test_cases}")
remove_data = test_cases.pop()
remove_case1 = test_cases.pop(1)
print(
    f"最终列表为:{test_cases},第一次删除的元素为:{remove_data},第二次删除的元素为:{remove_case1}，最终长度为{len(test_cases)}")

print("————————————————————————练习三：append() 与 extend()——————————————————————————")
# 定义：
# cases_a = ["login"]
# cases_b = ["login"]
# new_cases = ["register", "logout"]
#
# 分别执行：
# cases_a.append(new_cases)
# cases_b.extend(new_cases)
#
# 打印：
# 两个列表
# 两个列表长度
# 两个列表最后一个元素
# 两个列表最后一个元素的类型
# 注释回答：
# append() 添加了几个元素？
# 为什么 cases_a 的长度为 2？
# 为什么 cases_b 的长度为 3？
# extend() 是否一定只能传入列表？
# 第 4 题不确定时可以先写“待确认”，不要查新知识。
cases_a = ["login"]
cases_b = ["login"]
new_cases = ["register", "logout"]
cases_a.append(new_cases)
print(f"case_a:{cases_a},长度为{len(cases_a)},最后一个元素类型为:{type(cases_a[-1])}")
cases_b.extend(new_cases)
print(f"case_b:{cases_b},长度为{len(cases_b)},最后一个元素类型为:{type(cases_b[-1])}")
# append()添加了一个元素
# 因为case_a只添加了一个元素，所以长度为2（添加的元素是一个列表，只占一个地址）
# 因为case_b是将new_cases里的元素分别加入case_b后面，加了两个元素，所以长度为3
# extend传入可迭代对象，例如如果传入字符串的话，会把字符串当成一个列表，把每个字符拆开分别插入

print("————————————————————————练习四：查询和统计——————————————————————————")
# 定义：
status_codes = [200, 201, 200, 404, 500, 200, 404, 401]
# 完成：
# 统计 200 出现次数。
# 统计 404 出现次数。
# 查找 500 第一次出现的位置。
# 查找 401 第一次出现的位置。
# 判断 201 是否存在。
# 判断 403 是否不存在。
# 打印列表长度。
#
# 不要把文字写成一个值、代码却判断另一个值。

print("200出现的次数为:", status_codes.count(200))
print(f"404出现的次数为:{status_codes.count(404)}")
print(f"500第一次出现的位置为:{status_codes.index(500)}")
print(f"401第一次出现的位置为:{status_codes.index(401)}")
print(f"201 是否存在:{201 in status_codes}")
print(f"403 是否不存在:{403 not in status_codes}")
print(f"列表长度为:{len(status_codes)}")

print("————————————————————————练习五：排序与反转——————————————————————————")
# 定义：
response_times = [320.5, 85.2, 170.8, 95.6, 410.3]
# 完成：
# 使用 sorted() 得到升序新列表。
# 使用 sorted(..., reverse=True) 得到降序新列表。
# 打印原列表，确认没有变化。
# 定义另一个相同列表，对它使用 sort()。
# 保存并打印 sort() 的返回值。
# 使用切片得到倒序新列表。
# 定义另一个相同列表，对它使用 reverse()。
# 保存并打印 reverse() 的返回值。
# 比较切片倒序结果和 reverse() 后的原列表是否相等。
#
# 注意区分：
# 降序排序
# 反转当前顺序
sorted_response_time = sorted(response_times)
print(f"sorted_response_time:{sorted_response_time}")
reversed_response_time = sorted(sorted_response_time, reverse=True)
print(f"reversed_response_time:{reversed_response_time}")
print(f"原始列表:", response_times)

response_times2 = [320.5, 85.2, 170.8, 95.6, 410.3]
sort_result = sort_response = response_times2.sort()
print(response_times2)
print("切片得到的倒序新列表:", response_times2[::-1])

response_times3 = [320.5, 85.2, 170.8, 95.6, 410.3]
slice_times3 = response_times3[::-1]  #切片后的结果
reverse_result = response_times3.reverse()
print("reverse()后的结果为:", response_times3,"reverse()的返回值:", reverse_result)
print("切片倒序结果和reverse()后是否相等:", slice_times3 == response_times3)

print("————————————————————————练习六：数字列表统计——————————————————————————")

# 使用同一个 response_times 列表，计算并输出：
#
# 用例数量
# 最快响应时间
# 最慢响应时间
# 响应时间总和
# 平均响应时间
# 升序结果
#
# 三个时间类数据使用 f-string 保留两位小数。
#
# 不能修改原列表。
response_times = [320.5, 85.2, 170.8, 95.6, 410.3]
print(f"用例数量:{len(response_times)} | 最快响应时间:{min(response_times):.2f}ms | "
      f"最慢响应时间:{max(response_times):.2f}ms | 响应时间总和:{sum(response_times):.2f}ms |"
      f" 平均响应时间{sum(response_times)/len(response_times):.2f}ms")

print("响应时间升序结果为:",sorted(response_times))