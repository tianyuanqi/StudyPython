with open("test_result.txt", "w", encoding="utf-8") as file:
    file.write("login:PASS\n")
    file.write("user_info:PASS\n")
    file.write("eq:FAIL\n")

with open("test_result.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)

# Q1:
# 使用 "w" 模式打开一个已经存在的文件，
# 原来的内容会怎么样？
# A: 原来的内容会被清空

# Q2:
# write() 会不会自动换行？
# A: 不会自动换行，如果想换行需要自己加换行符\n