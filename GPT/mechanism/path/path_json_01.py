import json
from json import JSONDecodeError
from pathlib import Path


def load_user():
    current_dir = Path(__file__).resolve().parent
    file_path = (
            current_dir
            / "data"
            / "user.json"
    )

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            print(data)
            return data
    except FileNotFoundError as e:
        print(f"没找到文件:{e}")
        return None
    except JSONDecodeError as e:
        print(f"json解析异常:{e}")
        return None


user = load_user()

if user is not None:
    print(f"用户名:{user['username']}")
    print(f"角色:{user['role']}")

# Q1:
# load_user() 正常情况下返回什么类型？
# A: 返回字典类型


# Q2:
# 为什么这里不直接依赖
# Path.cwd() 来构造 user.json 的路径？
# A: 因为当前工作目录可能会发生变化，使用Path(__file__).resolve().parent获取文件路径再进行拼接会更合适


# Q3:
# 如果将来从不同目录启动这个脚本，
# 使用 __file__ 构造的路径是否仍然能定位
# 当前脚本旁边的 data/user.json？
# 为什么？
# A: 能定位，因为只要调用了load_user()方法，它就会先通过Path(__file__).resolve().parent
# 来找到当前文件的所在目录，也就是path这个文件夹，然后再通过字符串拼接来找到data文件下的user.json，
# 只要path/data/user.json这一层相对关系没有发生变化，就能定位到