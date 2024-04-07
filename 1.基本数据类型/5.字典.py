l1 = {1, 2, "三", 4}

d = {}  # 使用花括号来创建一个空字典
dict = {"hello": 2, 100: "world"}
print(dict["hello"])  # 打印数字2
print(dict[100])  # 打印字符串world
l1 = {1, 2, "三", 4}
dict = {"hello": 2, "str": "world", "list": l1}
print(dict)
print(dict["list"])
# print(dict["no"])  # 会报KeyError异常
dict["money"] = 111  # 如果dict中存在该key，则是修改，如果不存在该key，则新增
dict.update({"money": 100})  # 也可以通过update方法来修改key的值

# 删除键值对
dict = {"hello": 2, 100: "world"}
print("删除之前:", dict)
del dict["hello"]  # 通过del关键字来删除键值对
print("删除以后:", dict)

# 遍历字典
# 遍历键
dict = {"hello": 2, 100: "world"}
for key in dict:
    print("遍历键:",key)

# 遍历值
for value in dict.values():
    print("遍历值:",value)

#遍历键值对
for key, value in dict.items():
    print("遍历键值对:",key, value)

'''
Python 字典还提供了一些常用的方法，如：
    len()：返回字典中键值对的个数。
    keys()：返回字典中所有键的列表。
    values()：返回字典中所有值的列表。
    items()：返回字典中所有键值对的列表。
'''
print("字典dict键值对的个数为:", len(dict))
print("返回dict中所有键的列表:", dict.keys())
print("返回dict中所有值的列表:", dict.values())
print("返回dict中所有键值对的列表:", dict.items())
