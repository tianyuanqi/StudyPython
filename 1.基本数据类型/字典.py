
l1={1,2,"三",4}
dict={"hello":2,"str":"world","list":l1}

print(dict)
print(dict["list"])


'''
Python 字典还提供了一些常用的方法，如：
    len()：返回字典中键值对的个数。
    keys()：返回字典中所有键的列表。
    values()：返回字典中所有值的列表。
    items()：返回字典中所有键值对的列表。
'''
print("字典dict键值对的个数为:", len(dict))
print("返回dict中所有键的列表:",dict.keys())
print("返回dict中所有值的列表:",dict.values())
print("返回dict中所有键值对的列表:",dict.items())