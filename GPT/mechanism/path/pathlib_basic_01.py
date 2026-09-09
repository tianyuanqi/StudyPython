from pathlib import Path

file_path = Path("GPT/mechanism/path/data/user.json")

print(f"相对路径:{file_path}")
print(f"绝对路径:{file_path.resolve()}")
print(f"文件名:{file_path.name}")
print(f"去除后缀的文件名:{file_path.stem}")
print(f"后缀名:{file_path.suffix}")
print(f"当前文件所在目录:{file_path.parent}")
print(f"判断文件是否存在:{file_path.exists()}")
print(f"判断是不是文件:{file_path.is_file()}")

# Q1:
# name / stem / suffix 分别是什么？
# A:name是文件名,stem是获取去除后缀的文件名，suffix是获取文件后缀


# Q2:
# exists() 返回什么？
# A: 用于判断路径是否存在，如果存在返回True，不存在返回False


# Q3:
# is_file() 和 is_dir()
# 分别用于判断什么？
# A: is_file()判断是否是一个具体的文件，is_dir()判断是否是一个目录
