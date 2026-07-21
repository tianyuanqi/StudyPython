# 练习一：规范命名
from operator import and_

product_name = "键盘"  # 商品名称
product_price = 100  # 商品单价
product_quantity = 10  # 商品数量
salary = product_price * product_quantity  # 总价
error_messafe = None  # 错误信息

# 练习二：比较判断
total_cases = 100
executed_cases = 75
fail_cases = 5

print("已执行数量是否等于总数量:", total_cases == executed_cases)
print("失败数量是否大于:", fail_cases > 0)
print("通过数量是否不少于70:", executed_cases - fail_cases >= 70)
print("未执行数量是否小于 30:", (total_cases - executed_cases - fail_cases) < 30)

progress_percent = executed_cases / total_cases
print(type(progress_percent))
print("执行进度是否达到 80%:", progress_percent >= 0.8)
print("当前执行进度为", f"{progress_percent:.2%}")

# 练习三：测试结果组合判断
status_code = 200
response_time = 850
has_token = True
error_message = None
is_success = status_code == 200 and has_token==True and error_message is None

print("判定状态码为 200，并且响应时间不超过 1000 毫秒：", status_code == 200 and response_time <= 1000)
print("判定状态码不是 200，或者错误信息不为 None：", status_code != 200 or error_message is not None)
print("判定有 token，并且不存在错误信息：", has_token == True and error_message is None)
print("判定请求是否失败：对“请求成功条件”使用 not 取反:",not is_success)
