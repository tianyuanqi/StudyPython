import json


def load_json(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
          data = json.load(file)
    except FileNotFoundError:
        print("文件不存在")
        return None
    except json.JSONDecodeError:
        print("json格式错误")
        return None
    else:
        return data


print(load_json("user.json"))
print(load_json("broken.json"))
print(load_json("not_exist.json"))