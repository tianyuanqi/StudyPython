apps = [
    {
        "name": "王者荣耀",
        "category": "game",
        "is_ad": True
    },
    {
        "name": "微信",
        "category": "social",
        "is_ad": False
    },
    {
        "name": "和平精英",
        "category": "game",
        "is_ad": True
    }
]

# 使用循环统计游戏数量。
game_count = 0
for app in apps:
    if app["category"] == "game":
        game_count += 1

print("游戏的数量为:", game_count)

# 使用循环统计广告数量。
ad_count = 0
for app in apps:
    if app["is_ad"] is True:
        ad_count += 1
print(f"广告数量为:{ad_count}")

# 检查所有应用：如果缺少：name
# 输出：应用名称缺失

for index, app in enumerate(apps):
    if app["name"] == "":
        print(f"第{index+1}个应用名称缺失")

for app in apps:
    if app["category"] == "game":
        print(f"找到游戏应用:{app['name']}")
        break

check_pass = (
    game_count >= 2
    and ad_count >= 2
)
if check_pass:
    print("推荐结果检查通过")
else:
    print("推荐结果检查失败")