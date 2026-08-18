apps = [
    "微信",
    "支付宝",
    "淘宝",
    "抖音"
]
# 完成：
# 使用 for 遍历打印所有应用。
count = 0
for app in apps:
    print(app)
    count += 1
# 使用循环统计列表长度。
print(f"列表长度为:{count}")
# 使用 for 判断 "淘宝" 是否存在。
# 找到 "淘宝" 后使用 break 停止循环。
for app in apps:
    if app == "淘宝":
        print("淘宝存在")
        break


# 创建
empty_apps = [
    "微信",
    "",
    "淘宝"
]

# 使用 continue 跳过空字符串
for app in empty_apps:
    if(app == ""):
        continue
    print(app)

