import json
from json import JSONDecodeError


def load_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as e:
        print(f"发生异常:{e}，请检查文件是否存在")
        return []  # 必须return去终止程序，否则后面业务部分会继续执行并报错
    except JSONDecodeError as e:
        print(f"发生异常{JSONDecodeError}，请检查文件内容是否为json格式")
        return [] # 必须return去终止程序，否则后面业务部分会继续执行并报错
    else:
        return data
