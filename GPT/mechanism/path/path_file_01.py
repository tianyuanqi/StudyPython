from pathlib import Path

# 获取当前文件目录
current_dir = Path(__file__).resolve().parent

file_path = (
        current_dir / "data" / "user.json"
)

print(current_dir)
print(file_path)
print(file_path.exists())

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())


# Q1:
# Path(__file__).resolve().parent
# 最终得到什么？
# A:得到当前文件所在的目录


# Q2:
# 为什么这种方式比直接写
# "data/user.json"
# 更不容易受Working Directory影响？
# A:因为如果当前的工作路径发生改变以后，直接写"data/user.json"就会找不到文件而报错，
# 先获取当前文件的所在目录，再拼接"data/user.json"之后就不会有这个问题


# Q3:
# Path对象之间为什么可以使用 /
# 例如：
#
# current_dir / "data" / "user.json"
#
# A: 因为Path对象可以使用/拼接字符串形成新的路径