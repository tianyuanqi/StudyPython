list_A = [100, "hello", "world"]  # 这是一个列表
list_A[0] = 200  # 可以对列表中的任意元素进行重新赋值
print(f"修改后的列表为:{list_A}")

tuple_A = (100, "hello", "world")  # 这是一个元组
# tuple_A[0]=200  #执行到这里，就会报错
print(tuple_A)

tuple_A = ()  # 创建一个空元组
print(type(tuple_A))  # 结果为 <class 'tuple'>

tuple_h = ("hello")  # 这样创建就不是元组了
print(type(tuple_h))  # 结果为 <class 'str'>

tuple_one = (100)  # 这样创建也不是元组
print(type(tuple_one))  # 结果为 <class 'int'>

case_name = ("login",)  # 单元素元组，必须在里面保留一个逗号
print(type(case_name))  # 结果为 <class 'tuple'>

case_name = (100,)  # 这样写，也是创建一个元组
print(type(case_name))  # 结果为 <class 'tuple'>

print("————————————————————————练习一：元组创建、索引和切片————————————————————————")
test_cases = (
    "prepare_data",
    "user_login",
    "create_order",
    "pay_order",
    "user_logout"
)
# 完成：
# 打印完整元组。
# 打印类型。
# 打印长度。
# 打印第一个元素。
# 打印最后一个元素。
# 打印中间三个元素。
# 打印最后两个元素。
# 打印倒序后的新元组。
# 打印 test_cases[1] 的类型。
# 打印 test_cases[1:2] 的类型。
# 判断 "pay_order" 是否存在。
# 判断 "delete_order" 是否不存在。
#
# 要求：
# 使用索引、切片和成员运算完成。
# 不直接写死输出结果。
print(f"打印完整元组:{test_cases}")
print(f"打印类型:{type(test_cases)}")
print(f"打印长度:{len(test_cases)}")
print(f"打印第一个元素:{test_cases[0]}")
print(f"打印最后一个元素:{test_cases[-1]}")
print(f"打印中间三个元素:{test_cases[1:4]}")
print(f"打印最后两个元素:{test_cases[-2:]}")
print(f"打印倒序后的新元组:{test_cases[::-1]}")
print(f"打印 test_cases[1] 的类型:{type(test_cases[1])}")
print(f"打印 test_cases[1:2] 的类型:{type(test_cases[1:2])}")
print(f"判断 'pay_order' 是否存在:{'pay_order' in test_cases}")
print(f"判断 'delete_order' 是否不存在:{'delete_order' not  in test_cases}")

print("————————————————————————练习二：单元素元组和查询————————————————————————")
data_a = ("login")
data_b = ("login",)
data_c = ()
# 打印：
# data_a 及其类型。
# data_b 及其类型。
# data_c 及其类型。
# 三个对象的长度。

print("data_a:", data_a)
print("typea的类型为:", type(data_a))
print("data_b:", data_b)
print("typeb的类型为:", type(data_b))
print("data_c:", data_c)
print("typec的类型为:", type(data_c))
print("data_a的长度为:", len(data_a))
print("data_b的长度为:", len(data_b))
print("data_c的长度为:", len(data_c))

status_codes = (200, 201, 200, 404, 500, 200, 404)
# 打印：
# 统计 200 出现的次数。
# 统计 404 出现的次数。
# 查找 500 第一次出现的位置。
# 判断 201 是否存在。
# 判断 403 是否不存在。
# 打印元组长度。

print("200出现的次数为:", status_codes.count(200))
print("404出现的次数为:", status_codes.count(404))
print("500第一次出现的位置为:", status_codes.index(500))
print("201是否存在:",201 in status_codes)
print("403是否不存在:",403 not in status_codes)
print("元组长度为:",len(status_codes))


print("————————————————————————练习三：列表与元组对比————————————————————————")

list_cases = ["login", "register", "logout"]
tuple_cases = ("login", "register", "logout")
# 打印两个对象及其类型。
print(f"list_cases:{list_cases},类型为:{type(list_cases)}")
print(f"tuple_cases:{tuple_cases},类型为:{type(tuple_cases)}")

# 打印两个对象的第一个元素。
print(f"list_case第一个元素为:{list_cases[0]}")
print(f"tuple_case第一个元素为:{tuple_cases[0]}")

# 分别切出最后两个元素，并打印结果和类型。
print(f"list_case最后两个元素为:{list_cases[-2:]},类型为{type(list_cases[-2:])}")
print(f"tuple_case最后两个元素为:{tuple_cases[-2:]},类型为{type(tuple_cases[-2:])}")

# 将 list_cases[1] 修改为 "user_register"。
list_cases[1] = "user_register"
print("修改后的list:", list_cases)

# 打印修改后的列表。
# 将下面代码保留为注释，不直接运行：
# tuple_cases[1] = "user_register",取消注释后运行会报错，因为元组是无法被改变的
# 在注释中说明取消注释后会发生什么。


# 判断两个对象中是否都包含 "login"。
# 分别统计 "login" 出现的次数。
print(f"list_cases是否包含login:{'login' in list_cases},login出现的次数为:{list_cases.count('login')}")
print(f"tuple_cases是否包含login:{'login' in tuple_cases},login出现的次数为:{tuple_cases.count('login')}")




# 1. 单元素元组为什么必须加逗号？
# A 必须通过加逗号才能表示创建的是一个元组，否则将会是其他的数据类型

# 2. 元组索引与列表索引是否相同？
# A 用法基本相同，但列表可以通过索引进行重新赋值，元组不可以

# 3. 元组切片返回什么类型？
# 返回一个元组

# 4. 元组能否通过索引修改？
# 不能通过索引修改

# 5. 元组是否有 append()？
# 没有append方法

# 6. count() 会不会修改元组？
# count只返回出现的次数，并不会修改元组

# 7. index() 返回什么？
# 返回元素第一次出现时的索引位置，找不到时会抛出ValueError

# 8. 元组和列表当前最重要的区别是什么？
# 元组是不可修改的，列表可以修改

# 9. 哪类数据更适合使用元组？
# 定义之后不会被修改的数据更适合使用元组，比如个人身份信息，idcard等
