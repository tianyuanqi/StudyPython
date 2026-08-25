# 计算所有数字之和
def calculate_total(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

result_1 = calculate_total(10, 20)
result_2 = calculate_total(10, 20, 30, 40)
print(result_1)
print(result_2)


# 只要任何一个值为False，那么返回False
def all_pass(*results):
    for result in results:
        if result == False:
            return False

    return True

check_1 = all_pass(True, True, True)
check_2 = all_pass(True, False, True)
print(check_1)
print(check_2)

# Q1: *args 接收到的数据是什么类型？
# A: 是一个元组

# Q2: *args 适合解决什么问题？
# A: 适合解决不确定有多少入参的情况