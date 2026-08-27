import json

json_text = '{"status_code": 200, "business_code": 0, "token": "abc123"}'

data = json.loads(json_text)

print(data)
print(type(data))

json_result = json.dumps(data, ensure_ascii=False)
print(json_result)
print(type(json_result))


# Q1:
# json.load() 和 json.loads() 最大区别是什么？
# A: load是直接读取文件，把文件内容转换成python对象（通常是字典）
#  loads是把json类型的字符串，转换成python对象（字典）

# Q2:
# json.dump() 和 json.dumps() 最大区别是什么？
# A: dump是直接把python对象写入文件
# dumps是把python对象，转换成字符串，并不会写入文件