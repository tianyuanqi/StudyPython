def print_request_info(**kwargs):
    for key, value in kwargs.items():
        print(key, value)


print_request_info(
    method="POST",
    url="/login",
    timeout=5
)

print("————————————————分割线————————————————")


# 如果存在：timeout，返回对应值。如果不存在，返回：5
def get_timeout(**kwargs):
    return kwargs.get("timeout",5)


time_out1 = get_timeout(timeout=10)
time_out2 = get_timeout(method="GET")
print(time_out1)
print(time_out2)

# Q1: **kwargs 接收到的数据是什么类型？
# A: 字典

# Q2: *args 和 **kwargs 最大区别是什么？
# A: args接受不确定数量的位置参数，返回一个元组
#  kwargs接受不确定数量的关键字参数，返回一个字典