status_codes = {200, 300, 400, 200, 300, 500}

# print(status_codes)

# 用集合检查重复数据

app_ids = [404, 402, 200, 400, 500, 404, 401, 402, 404]
unique_app_ids = set(app_ids)  # 将列表转为集合，自动去重
print(unique_app_ids)

print("原列表中是否存在重复元素:", len(app_ids) != len(unique_app_ids))  # 原列表长度!=去重后的长度

# 创建普通集合
environments = {"test", "pre", "prd", "test"}
print("environments:", environments)

status_codes = set([200, 400, 400, 404])
print("status_codes:", status_codes)

status_codes = set((200, 400, 402, 404, 402))
print("status_codes:", status_codes)

# 创建空集合
empty_data = {}

# print(environments[1])

print("——————————————————————————练习一：集合基础——————————————————————————")
status_codes = {200, 201, 200, 404, 500, 404}
# 打印完整集合。
print("完整集合status_codes:", status_codes)
# 打印类型。
print("status_codes的类型为:", type(status_codes))
# 打印长度。
print(f"status_codes的长度为:{len(status_codes)}")
# 判断 200 是否存在。
print(f"status_codes中是否存在200:{200 in status_codes}")

# 判断 403 是否不存在。
print(f"status_codes中是否不存在403:{403 not in status_codes}")

# Q 解释为什么原数据有六个值，集合长度却不是六。
# A 因为集合具有去重的特点，重复的元素不会被加入集合

# 创建空集合并打印其类型。
empty_set = set()

# 创建：empty_data = {} 打印它的类型，并说明它为什么不是集合。
empty_data = {}
print(type(empty_data))  # empty是一个空的字典

case_list = [
    "login",
    "register",
    "login",
    "logout",
    "register"
]
# 将列表转换为集合。
set_list = set(case_list)
# 打印转换后的集合。
print("转换后的set_list:", set_list)

# 比较转换前后长度。
print(f"转换前的长度:{len(case_list)},转换后的长度:{len(set_list)}")

# 创建变量判断原列表是否有重复数据。
has_duplicate_data = len(set_list) != len(case_list)

# 确认原列表没有被修改。
print("原列表有没有被修改:",case_list!=[ "login",
    "register",
    "login",
    "logout",
    "register"])