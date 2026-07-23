print("—————————————————————练习一：商品结算信息———————————————————————————————")
product_name = "机械键盘"
unit_price = 299.9
quantity = 2
# 要求：
# 计算商品总价。
# 使用一个 f-string 打印完整信息。
# 单价和总价均保留两位小数。
# 输出格式类似：
# 商品：机械键盘，单价：299.90 元，数量：2，总价：599.80 元
# 不能直接写死计算结果。

print(f"商品:{product_name}，单价:{unit_price}元，"
      f"数量:{quantity},商品总价为:{(unit_price * quantity):.2f}")

print("—————————————————————练习二：测试执行报告———————————————————————————————")
#
# 定义：
# total_cases = 120
# executed_cases = 96
# failed_cases = 6
#
# 要求计算：
# 通过数量
# 未执行数量
# 执行进度
# 通过率
#
# 然后使用 f-string 输出：
#
# 总用例：120
# 已执行：96
# 通过：90
# 失败：6
# 未执行：24
# 执行进度：80.00%
# 通过率：93.75%
#
# 注意：
# 通过率以“已执行用例”为分母。
# 执行进度以“总用例”为分母。
# 百分比变量保存为 0～1 之间的小数。
# 不使用 if/else。
total_cases = 120
executed_cases = 96
failed_cases = 6
print(f"总用例:{total_cases}")
print(f"已执行:{executed_cases}")
print(f"通过数量:{executed_cases - failed_cases}")
print(f"失败数量:{failed_cases}")
print(f"未执行数量:{total_cases - executed_cases}")
print(f"执行进度:{(executed_cases/total_cases):.2%}")
print(f"通过率:{(executed_cases-failed_cases)/executed_cases:.2%}")



print("—————————————————————练习三：格式化测试用例编号———————————————————————————————")

# 定义：
case_number = 7
api_name = "login"
status_code = 200
response_time = 86.378

# 要求生成并打印：
# CASE_007 | login      | 200 | 86.38 ms
# 要求：
# 用例编号宽度为三位，不足补零。
# 接口名称占十个字符宽度，并左对齐。
# 响应时间保留两位小数。
# 整行使用一个 f-string 完成。
# 修改 case_number 为 35，确认仍能正常显示。

print(f"CASE_{case_number:03d} | {api_name:<10} | {status_code:.2f} | {response_time}")


print("—————————————————————练习四：思考题———————————————————————————————")

#Q: f-string 前面的 f 有什么作用？
#A: f表示当前是格式化字符串，可以在后面的{}里填入变量或进行计算

#Q {value:.2f} 中的 .2f 表示什么？
#A 表示把当前变量转为浮点数并保留两位小数

#Q {rate:.2%} 是否需要提前把 rate 乘以 100？
#A 不需要，会自动乘100，然后加上%，再保留两位小数

#Q {number:03d} 表示什么？
#A 表示number变量长度为3，按整数显示，如果不够的话在前面用0去补齐

#Q 格式化显示两位小数后，原变量的值是否改变？
#A 不会改变，数字是不可修改数据类型，格式化显示两位小数是创建了一个新的变量

#Q <、>、^ 分别表示什么对齐方式？
#A 表示左对齐，右对齐，和居中对齐

#Q f-string 的花括号中能否进行简单计算？
#A 可以进行简单计算

#Q 为什么复杂计算通常建议先保存到变量，再放进 f-string？
#A 因为复杂变量计算步骤比较多，都放在一行里面可读性比较差

