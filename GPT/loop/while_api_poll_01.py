# 模拟异步任务接口
# 定义：
task_statuses = [
    "processing",
    "processing",
    "processing",
    "success"
]
max_retry = 5
retry_count = 0
index = 0

# 要求使用while完成轮巡，每次输出task_statuses[index]
# 并打印
# 第1次查询，任务状态：processing
# 第2次查询，任务状态：processing
# 第3次查询，任务状态：processing
# 第4次查询，任务状态：success
# 如果status == "success"，打印任务执行成功

while index < len(task_statuses) and retry_count < max_retry:
    print(f"第{index + 1}次查询，任务状态{task_statuses[index]}")
    if task_statuses[index] == "success":
        print("任务执行成功")
        break
    index += 1
    retry_count += 1

print("————————————————————分割线————————————————————")
failed_statuses = [
    "processing",
    "processing",
    "processing",
    "processing",
    "processing"
]
index = 0
max_retry = 3

# 要求：只查询前三次。三次都没有 "success" 后输出：超过最大轮询次数，任务未完成

task_success = False
while True:
    if index < max_retry:
        print(f"第{index + 1}次查询, 状态{failed_statuses[index]}")
        if failed_statuses[index] == "success":
            task_success = True
            print("任务成功")
            break
        index += 1
    else:
        print("超过最大轮训次数，任务未完成")
        break

if task_success:
    print("测试成功")
else:
    print("测试失败")

# Q1:
# 为什么接口轮询不能简单写成：
#
# while status != "success":
#     查询接口
#
# A: 除非会在后面修改status状态或者使用break，否则很容易造成死循环


# Q2:
# 为什么接口自动化中的轮询一般要设置最大次数或超时时间？
# A: 因为如果不做限制，出现死循环之后整个任务无法继续进行下去


# Q3:
# 已知有10条测试数据需要全部执行，更适合 for 还是 while？为什么？
# A: 更适合for，因为测试数据是已知的，只需要从头到尾遍历一遍即可，不需要判断状态


# Q4:
# 一个OTA任务不知道多久才能完成，需要不断查询升级状态，
# 更适合 for 还是 while？为什么？
# A: 更适合while循环，因为任务时间是不确定的，用可以用升级状态作为判断，然后循环等待，增加超时时间限制，升级成功或者达到超时时间后结束
