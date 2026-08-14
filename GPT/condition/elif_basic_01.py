# 200 → 请求成功
# 400 → 请求参数错误
# 401 → 未授权
# 404 → 资源不存在
# 500 → 服务端异常
# 其他 → 未知状态码
# 要求：
# 只打印一条最终结果。
# 不能写成 5 个独立 if。

status_code = 404

if status_code == 200:
    print("请求成功")
elif status_code == 400:
    print("请求参数错误")
elif status_code == 401:
    print("未授权")
elif status_code == 404:
    print("资源不存在")
elif status_code == 500:
    print("服务端异常")
else:
    print("未知状态码")

# 定义：
response_time = 850
# 划分
# <= 300       → 非常快
# 301 ~ 500    → 正常
# 501 ~ 1000   → 较慢
# > 1000       → 超时风险

if response_time <= 300:
    print("非常快")
elif response_time <= 500:
    print("正常")
elif response_time <= 1000:
    print("较慢")
elif response_time > 1000:
    print("超时风险")