print("————————————————————————————————练习二：集合增删——————————————————————————————————————————")
test_cases = {
    "login",
    "register",
    "logout"
}
print(f"初始test_cases:{test_cases}")

# 使用 add() 添加 "profile"。
test_cases.add("profile")
print("添加profile以后的test_cases:", test_cases)

# 再次添加 "login"，观察长度是否变化。
print(f"添加login之前的长度为:{len(test_cases)}")
test_cases.add("profile")
print(f"添加login之后的长度为:{len(test_cases)}")
print(f"添加login之后的test_cases:{test_cases}")

# 使用 update() 批量添加：["update_user", "delete_user"]
test_cases.update(["update_user", "delete_user"])
print(f"使用update()批量添加以后:{test_cases}")

# 使用 remove() 删除 "logout"。
test_cases.remove("logout")
print(f"使用remove()删除logout之后:{test_cases}")

# 使用 discard() 删除 "register"。
test_cases.discard("register")
print(f"使用discard()删除register以后:{test_cases}")

# 再次使用 discard() 删除不存在的 "register"。
test_cases.discard("register")
print(f"第二次删除register以后:{test_cases}")

# 使用 pop() 删除一个元素并保存返回值。
remove_data = test_cases.pop()

# 打印最终集合、删除的元素和集合长度。
print(f"最终集合为:{test_cases}")
print(f"被pop删除的元素为:{remove_data}")
print(f"最终集合的长度为{len(test_cases)}")


# 在注释中回答：
#
#Q 集合是否有 append()？
#A 集合没有append() 方法

#Q add() 和 update() 的区别是什么？
#A add只能添加一个元素，update是接收可迭代对象，对其内容进行批量添加

#Q remove() 和 discard() 的区别是什么？
#A 如果删除的那个元素并不存在，remove()会报错keyError，discard不会报错

#Q 为什么集合 pop() 无法预先确定删除哪个元素？
#A 因为集合是无序的，只能随机进行删除

#Q add() 重复元素后为什么长度不变？
#A 因为集合具有去重的特性，发现重复的元素，并不会被加入集合

#Q 集合 pop() 与列表、字典 pop() 的区别。
#A 列表、字典的pop()是默认删除最后一个元素，返回被删除的内容
#A 集合pop()是随机删除一个元素，返回被删除的内容

#Q 集合为什么不能使用索引。
#A 集合是无序的数据结构，没有位置概念，无法使用索引

# 空集合为什么必须使用 set()。
# 因为如果不直接赋值的话，使用set={} 创建的是一个字典

#Q 并集、交集、差集、对称差集。
#A 并集使用set1 | set2 ,交集使用 set1 & set2 差集使用 set1 - set2 对称差集表示只在其中一边出现 set1 ^ set2

#Q 集合在接口测试中的用途。
#A 可以用来检查返回内容是否存在重复
#A 检查响应内容缺少哪些字段
#A 检查状态码是否合法