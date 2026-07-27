test_cases = [
    "user_login",
    "user_register",
    "user_logout",
    "user_profile"
]
# 要求打印：
# 完整列表。
# 列表类型。
# 列表长度。
# 第一个元素。
# 最后一个元素。
# 第二个元素。
# 最后两个元素。
# 倒序后的列表。
# "user_login" 是否存在。
# "delete_user" 是否不存在。
# 要求：
# 必须通过索引、切片和成员运算完成。
# 不能直接写死输出结果。
print("完整列表:", test_cases)
print("列表类型:", type(test_cases))
print("列表长度:", len(test_cases))
print("列表第一个元素:", test_cases[0])
print("列表最后一个元素:", test_cases[-1])
print("列表第二个元素:", test_cases[1])
print("列表最后两个元素:", test_cases[-2:])
print("倒序后的列表:", test_cases[::-1])
print("user_login是否存在:", "user_login" in test_cases)
print("delete_user是否不存在:", "delete_user" not in test_cases)

print("———————————————练习二：修改和添加测试用例—————————————————————")

# 初始列表：test_cases = ["login", "register", "logout"]
# 依次完成：
# 将 "register" 修改为 "user_register"。
# 使用 append() 添加 "profile"。
# 使用 insert() 将 "health_check" 插入列表开头。
# 使用 extend() 添加：
# ["update_user", "delete_user"]
# 每完成一步都打印列表。
# 最后打印列表长度。
#
# 禁止直接重新给整个列表赋值完成修改。
test_cases = ["login", "register", "logout"]
test_cases[1] = "user_register"
print("修改register以后的列表:", test_cases)
test_cases.append("profile")
print("添加以后得列表:", test_cases)
test_cases.insert(0, "health_check")
print("使用 insert() 将 health_check 插入列表开头以后:", test_cases)
test_cases.extend(["update_user", "delete_user"])
print("使用extend添加以后:", test_cases)
print("最终test_case的长度:", len(test_cases))

print("———————————————练习三：删除测试结果————————————————————")

# 定义：
# test_results = [
#     "login_success",
#     "register_success",
#     "logout_failed",
#     "profile_success"
# ]
# 完成：
# 使用 remove() 删除 "register_success"。
# 使用 pop() 删除最后一个元素，并保存返回值。
# 使用 pop(1) 删除索引 1 的元素，并保存返回值。
# 打印每次删除后的列表。
# 打印两个由 pop() 返回的元素。
# 打印最终列表长度。
# 在注释中说明：remove() 和 pop() 的主要区别是什么？
test_results = [
    "login_success",
    "register_success",
    "logout_failed",
    "profile_success"
]
test_results.remove("register_success")
print("删除register_success以后的值:", test_results)

end_data = test_results.pop(-1)
print("删除最后一个元素后的值:", test_results)

index_1_data = test_results.pop(1)
print("删除索引为1的值以后:", test_results)
print("刚才删除的最后一个元素为:", end_data)
print("刚才删除的index为1的元素为:", index_1_data)
print("最终列表长度为:", len(test_results))
# remove()是直接删除对应的元素，没有返回值。pop()是在删除对应元素以后，把被删除的内容作为返回值返回


print("———————————————练习四：append() 与 extend() 对比————————————————————")
# 分别定义两个相同列表：
# cases_a = ["login"]
# cases_b = ["login"]
# new_cases = ["register", "logout"]
#
# 然后：
# cases_a.append(new_cases)
# cases_b.extend(new_cases)
#
# 打印：
# cases_a
# cases_b
# 两个列表的长度
# cases_a 最后一个元素的类型
# cases_b 最后一个元素的类型

# 在注释中回答：
# 为什么 append() 和 extend() 的结果不同？
# append()是在列表后面增加一个元素，这个元素可以是一整个列表
# extend()是在列表后面一次增加多个元素，如果添加的是一个列表的话，相当于把两个列表进行了拼接
# cases_a =["login",["register","logout"]]，长度为2，最后一个元素类型是list
# cases_b =["login","register","logout"]，长度为3，最后一个元素类型是str

cases_a = ["login"]
cases_b = ["login"]
new_cases = ["register", "logout"]
cases_a.append(new_cases)
cases_b.extend(new_cases)
print("打印cases_a:", cases_a,"长度为:",len(cases_a)," 最后一个元素类型是:",type(cases_a[-1]))
print("打印cases_b:", cases_b,"长度为:",len(cases_b)," 最后一个元素类型是:",type(cases_b[-1]))


# 写在代码末尾，使用 # 注释回答：
#Q 列表索引和字符串索引的规则是否相同？
#A 规则相同

#Q data[0] 与 data[0:1] 的返回类型为什么可能不同？
#A data[0]得到的返回值是一个元素，这个元素是什么类型返回值就是什么类型，data[0:1]返回值是只有一个元素的列表，返回类型固定是list

#Q 列表能否通过索引修改元素？
#A 可以，列表是可变数据类型，可以根据索引修改里面的元素

#Q append() 每次添加几个元素？
#A 每次添加一个元素

#Q extend() 如何处理传入列表中的元素？
#A 会把列表中的元素分别加入

#Q remove() 按照索引还是元素内容删除？
#A 按照元素内容删除

#Q pop() 是否会返回被删除的元素？
#A 会返回被删除的元素

#Q pop() 不传索引时删除哪个元素？
# 不传索引时默认删除最后一个元素

#Q 列表切片会得到单个元素还是新列表？
#A 得到一个新的列表

#Q 为什么字符串不能通过索引修改，而列表可以？
#A 因为str是不可变数据类型，列表是可变数据类型

