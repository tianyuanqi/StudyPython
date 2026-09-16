names = [
    "alice",
    "bob",
    "jack"
]

roles = [
    "admin",
    "tester",
    "user"
]
users = zip(names, roles)
print(next(users))
print(next(users))
print(list(users))
print(list(users))  # 迭代器已经被用完了，输出为空

# 重新创建
users = zip(names, roles)

for name, role in users:
    print(f"姓名:{name},角色:{role}")

indexed_names = enumerate(names, start=1)
print(next(indexed_names)) # 输出1,alice
print(next(indexed_names)) # 输出2,bob

# Q1:
# zip() 返回的是列表吗？
# A: 不是列表，返回的是一个迭代器


# Q2:
# 为什么对同一个zip对象调用
# 第二次list(users)时可能得到[]？
# A: 因为前面的操作会让迭代器往后去访问下一个元素，在第二次list(users)时已经没有元素，迭代器被用完了


# Q3:
# 如果想重新遍历zip中的全部数据，
# 应该怎么办？
# A: 可以再创建一个新的迭代器


# Q4:
# enumerate() 返回的对象
# 为什么也可以使用next()？
# A: 因为enumerate()返回的也是一个迭代器