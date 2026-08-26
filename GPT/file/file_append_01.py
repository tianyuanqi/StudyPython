with open("test_result.txt", "a", encoding="utf-8") as file:
    file.write("ota:PASS\n")

with open("test_result.txt", "r", encoding="utf-8") as file:
    result = file.read()
    print(result)

# Q1:
# "w" 和 "a" 最大区别是什么？
# A: w是清空文件内容，a是在文件末尾增加

# Q2:
# 如果使用 "a" 模式，而文件不存在，会发生什么？
# A: 会新建一个文件，然后把内容写进去（如果代码里有写入内容的话）