required_fields = {
    "code",
    "message",
    "data",
    "request_id"
}

actual_fields = {
    "code",
    "message",
    "data",
    "timestamp"
}
# 分别计算并打印：
#
# 两组字段共有的字段。
print(f"两组字段共有的字段为:{required_fields & actual_fields}")

# 所有出现过的字段。
print(f"所有出现过的字段为:{required_fields | actual_fields}")

# 必需但实际缺少的字段。
print(f"必须但实际缺少的字段为:{required_fields - actual_fields}")

# 实际多出来的字段。
print(f"实际多出来的字段为:{actual_fields - required_fields}")

# 只存在于其中一组的字段。
print(f"只存在其中一组的字段为:{actual_fields ^ required_fields}")

# "data" 是否存在于实际字段。
print(f"实际字段中是否存在data:{'data' in actual_fields}")

# "token" 是否不存在于实际字段。
print(f"实际字段中是否没有token:{'token' not in actual_fields}")

# 实际字段是否与必需字段完全相等。
print(f"实际字段是否与必须字段完全相等:{actual_fields == required_fields}")

returned_app_ids = [
    101,
    102,
    103,
    104,
    102,
    105
]
# 应用总数量。
print(f"应用总量为:{len(returned_app_ids)}")
# 去重后的应用集合。
print(f"去重后的应用集合:{set(returned_app_ids)}")
# 去重后的数量。
print(f"去重后的数量为:{len(set(returned_app_ids))}")
# 是否存在重复应用。
print(f"是否存在重复应用:{len(returned_app_ids) != len(set(returned_app_ids))}")

# 重复前后数量相差多少。
print(f"重复前后数量相差多少:{len(returned_app_ids) - len(set(returned_app_ids))}")
