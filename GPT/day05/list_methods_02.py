print("————————————练习一：状态码统计与查询——————————————————")
# 定义：status_codes = [200, 201, 200, 404, 500, 200, 404]
#
# 完成：
# 打印原列表。
# 统计 200 出现的次数。
# 统计 404 出现的次数。
# 查找 500 第一次出现的索引。
# 判断 201 是否在列表中。
# 判断 403 是否不在列表中。
# 打印列表长度。
status_codes = [200, 201, 200, 404, 500, 200, 404]
print("原始列表为:", status_codes)
print("200出现的次数为:", status_codes.count(200))
print("404出现的次数为:", status_codes.count(404))
print("500第一次出现的索引为:", status_codes.index(500))
print("201是否在列表中:", 200 in status_codes)
print("403是否不在列表中:", 403 not in status_codes)
print("列表长度为:", len(status_codes))

print("————————————练习二：响应时间排序——————————————————")

# 定义：response_times = [320.5, 85.2, 170.8, 95.6, 410.3]
#
# 完成：
# 打印原始列表。
# 使用 sorted() 得到升序新列表。
# 再次打印原列表，确认没有变化。
# 使用 sorted(..., reverse=True) 得到降序新列表。
# 打印最小响应时间。
# 打印最大响应时间。
# 计算平均响应时间。
# 平均响应时间使用 f-string 保留两位小数。
#
# 不能直接写死排序结果或平均值。
response_times = [320.5, 85.2, 170.8, 95.6, 410.3]
print("原始列表为:", response_times)
print("列表改为升序:", sorted(response_times))
print("改为升序以后原始列表为:", response_times, "原始列表是否有变化:",
      response_times != [320.5, 85.2, 170.8, 95.6, 410.3])
reverse_response_times = sorted(response_times, reverse=True)
print("降序列表为:", reverse_response_times)

print("最小响应时间为:", min(response_times))
print("最大响应时间为:", max(response_times))

avg_response_time = sum(response_times) / len(response_times)
print(f"平均响应时间为:{avg_response_time:.2f}ms")

print("————————————练习三：sort() 与 sorted() 对比——————————————————")
# 分别定义：
numbers_a = [30, 10, 40, 20]
numbers_b = [30, 10, 40, 20]
#
# 完成：
# 对 numbers_a 使用 sort()。
# 保存并打印 sort() 的返回值。
# 对 numbers_b 使用 sorted()，将结果保存到新变量。
# 打印：
# numbers_a
# sort() 的返回值
# numbers_b
# sorted() 的结果

# 在注释中回答：
#
# 为什么 sort() 的返回值是 None，而 sorted() 可以保存排序结果？
# 只需从使用结果角度解释：
# sort() 负责修改原列表。
# sorted() 负责返回新的排序列表。
# 暂不展开内部设计原理。
sort_a = numbers_a.sort()
sort_b = sorted(numbers_b)
print("number_a:", numbers_a)
print("number_b:", numbers_b)
print("sort_a:", sort_a)
print("sort_b:", sort_b)
# 因为sort()直接改变原始列表，所以返回None，sorted()是创建一个新的列表然后进行排序


print("————————————练习四：反转测试执行顺序——————————————————")

# 定义：
execution_order = [
    "prepare_data",
    "login",
    "create_order",
    "pay_order",
    "logout"
]
# 完成：
# 使用切片得到倒序新列表。
# 打印原列表，确认没有变化。
# 使用 reverse() 反转原列表。
# 打印反转后的原列表。
# 保存并打印 reverse() 的返回值。
# 判断两种反转结果是否相等。

# 在注释中回答：
# 切片[::-1]和 reverse() 的主要区别是什么？
print("切片得到的新列表:", execution_order[::-1])
print("原始列表为:", execution_order)
reverse_order = execution_order.reverse()
print("翻转列表为", reverse_order)
print("原始列表为", execution_order)
print("两种反转是否相等:", execution_order[::-1] == reverse_order)
# [::-1]是切片，会得到一个新的列表，reverse()是修改原有的列表进行反转



print("————————————练习四：反转测试执行顺序——————————————————")

# 定义：
# case_times = [125.5, 320.8, 98.2, 210.4, 150.0]
#
# 输出一份简单报告：
#
# 用例数量：5
# 最快响应：98.20 ms
# 最慢响应：320.80 ms
# 平均响应：180.98 ms
# 升序结果：[98.2, 125.5, 150.0, 210.4, 320.8]
#
# 要求：
# 使用 len()、min()、max()、sum()、sorted()。
# 三个响应时间均使用 f-string 保留两位小数。
# 原列表不能被修改。
# 不使用循环和条件判断。
case_times = [125.5, 320.8, 98.2, 210.4, 150.0]
print("这是一份测试报告:")
print(f"最快响应:{min(case_times):.2f}ms")
print(f"最慢响应:{max(case_times):.2f}ms")
print(f"平均响应:{sum(case_times)/len(case_times)}ms")
print(f"升序结果:{sorted(case_times)}")
print("原始列表:",case_times)


# 六、思考题
# 写在 list_methods_02.py 末尾，使用 # 回答：
#Q count() 会不会修改原列表
#A 不会修改原始列表

#Q index() 找不到元素时会发生什么？
#A 会报错，ValueError

#Q sort() 会不会修改原列表？
#A 会修改原始列表

#Q sort() 的返回值是什么？
#A 返回值是None

#Q sorted() 会不会修改原列表？
#A 不会修改原始列表

#Q sorted() 返回什么类型？
#A 里面传入的是什么类型就返回什么类型，传入List就返回List

#Q reverse() 是排序还是反转顺序？
#A 反转顺序

#Q reverse() 会不会修改原列表？
#A 会修改原始列表

#Q data[::-1] 会不会修改原列表？
#A 不会修改，切片是新增一个列表

#Q sort(reverse=True) 表示什么？
#A 表示把原始列表改为倒序排列
