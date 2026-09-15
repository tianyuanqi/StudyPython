cases = [
    {
        "case_name": "login_success",
        "business_code": 0
    },
    {
        "case_name": "wrong_password",
        "business_code": 1001
    },
    {
        "case_name": "wrong_username",
        "business_code": 1001
    }
]
# 使用字典推导式得到
# case_codes = {
#     "login_success": 0,
#     "wrong_password": 1001,
#     "wrong_username": 1001
# }
case_codes = {
    case["case_name"]: case["business_code"]
    for case in cases
}
print(case_codes)

# 然后利用这些business_code再生成一个集合unique_codes，
# 结果应该只有{
#     0,
#     1001
# }
unique_codes = {
    code
    for code in case_codes.values()
}
print(unique_codes)


# Q1:
# 字典推导式与列表推导式最大的结果区别是什么？
# A: 字典推导式保存的是字典（键值对），列表推导式保存的是一个个的值，并且字典的key是不能重复的，而列表可以有重复


# Q2:
# 为什么 unique_codes 中两个1001
# 最终只剩一个？
# A: 因为集合具有去重的特性，只会保留一个1001