# 第一行python代码
print("hello world")

status_code = 200
print("请求成功", "返回码：" + str(status_code))

status_code2 = 401
message = "未经授权，访问服务器被拒绝"
print(message, "返回码：" + str(status_code2))

# 使用f-str写法
print(message, f"返回码：{status_code2}")

print(f"{message},返回码: {status_code2}")

'''
你的实战任务 💻
现在，模拟一个真实的测试场景：
假设你刚刚测试了一个登录接口，从服务端提取到了一个提示信息变量 error_msg = "密码错误"。
你能尝试写一段 if-else 结构的代码吗？ 判断 error_msg 是否等于 "成功"。如果是，打印 "登录测试通过"；如果不等于，打印出具体的错误信息（最好用上刚刚学的 f-string 终极形态哦）。
'''
error_msg = "密码错误"

if error_msg == "成功":
    print("登录成功")
else:
    print(f"登录失败，具体的错误信息为:{error_msg}")

'''
现在，让我们进入自动化测试的一个核心场景：批量执行 (Batch Execution)。
平时测试时，我们通常不会只测一条数据，而是会跑一组用例。在 Python 中，用来装一组数据的“大盒子”叫做列表 (List) 。列表用方括号 [] 表示，里面的数据用逗号隔开。
比如，我们有一组接口返回的状态码准备进行校验：
Python
status_codes = [200, 401, 404, 500]
为了让代码自动挨个处理列表里的这些状态码，我们需要用到 for-in 循环 。它的语法像这样 🔄：
Python
# code 是一个临时变量，每次循环它会自动变成列表里的下一个数字
for code in status_codes:
    print(f"正在处理状态码：{code}")

你的实战任务 💻：
我们要把刚刚学的“循环”和“条件判断”结合起来。
请你写一段代码，遍历 status_codes = [200, 401, 404, 500] 这个列表。在 for 循环的内部写一段 if-else 判断：
如果 code 等于 200，打印 "测试通过"。
否则，利用 f-string 打印 "测试失败，返回码为：{code}"。
(前辈的提示：既然 if-else 属于 for 循环的一部分，那么 if 和 else 也需要向右缩进哦！) 试着在你的编辑器里敲一下，然后把代码发给我看看。
'''
error_msgs = [200, 401, 404, 500]

for msg in error_msgs:
    if msg == 200:
        print("登录成功")
    else:
        print(f"登录失败，返回码为:{msg}")

'''现在，假设我们调用了一个查询用户信息的接口，返回的数据如下：'''
api_response = {
    "code": 404,
    "msg": "找不到该用户",
    "user_id": None
}
'''
你能尝试写一段代码吗？
从 api_response 字典中提取出 code 和 msg 的值，分别存到两个变量里。
写一个 if-else 判断：如果提取到的 code 等于 200，打印 "查询成功"；否则，利用 f-string 打印出 "查询失败，原因：{提取到的msg}"。
'''


def assert_response(api_response):
    code = api_response["code"]
    msg = api_response["msg"]
    if code == 200:
        #print("查询成功")
        return "查询成功"

    else:
        #print(f"查询失败，原因:{msg}")
        return f"查询失败，原因:{msg}"

print(f"开始运行函数，运行结果：{assert_response(api_response)}")