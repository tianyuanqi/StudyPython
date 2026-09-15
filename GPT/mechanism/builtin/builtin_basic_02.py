results = [
    True,
    True,
    False
]

# 分别打印:any(results),all(results),len(results)

print(any(results))  # True
print(all(results))  # False
print(len(results))  # 3

usernames = [
    "user01",
    "user02",
    "user03"
]

roles = [
    "admin",
    "tester",
    "user"
]
# zip()循环打印
# user01:admin
# user02:tester
# user03:user

users = zip(usernames, roles)
for i in users:
    print(i)

cases = [
    {
        "case_name": "case03",
        "priority": 3
    },
    {
        "case_name": "case01",
        "priority": 1
    },
    {
        "case_name": "case02",
        "priority": 2
    }
]

# 使用sorted和lambda来让cases按照priority从小到大排列
new_cases = sorted(
    cases,
    key=lambda case: case['priority']
)

print(new_cases)

# 使用enumerate(..., start=1)
# 打印
# 1:case01
# 2:case02
# 3:case03

for index, i in enumerate(new_cases, start=1):
    print(f"{index}:{i['case_name']}")

# Q1:
# any() 和 all() 的区别是什么？
# A: any() 表示只要有一个元素是True，整体就返回True。
#  All() 表示所有元素都是True，整体才会返回True


# Q2:
# zip() 的主要作用是什么？
# 如果两个列表长度不同会怎样？
# A: zip() 的主要作用是将两个不同的列表进行拼接，形成一个新的列表。如果两个列表的长度不一样，
# 会以较短的那个为基准，拼接到和它一样的长度


# Q3:
# sorted() 会直接修改原列表吗？
# A: 不会修改原列表，是返回一个新的列表


# Q4:
# lambda case: case["priority"]
# 在这里的作用是什么？
# A: 作用是返回字典中"priority"对应的那个value
