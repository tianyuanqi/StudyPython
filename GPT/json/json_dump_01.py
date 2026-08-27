import json

test_result = {
    "case_name": "登录接口测试",
    "status": "PASS",
    "response_time": 320
}

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(test_result, file, ensure_ascii=False, indent=4)

with open("result.json", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)


# Q1:
# json.dump() 的作用是什么？
# A: 往文件里面写入json数据

# Q2:
# ensure_ascii=False 有什么作用？
# A: 不让中文转为ascii码，保留可读性

# Q3:
# indent=4 有什么作用？
# A: 让代码进行缩进，增加可读性