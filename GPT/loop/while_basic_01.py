# 使用 while 输出：
# 1
# 2
# 3
# 4
# 5

count = 1
while count <= 5:
    print(count)
    count += 1

print("——————————————————分割线——————————————")
# 定义count = 5，输出
# 5
# 4
# 3
# 2
# 1
count = 5
while count >= 1:
    print(count)
    count -= 1

print("——————————while计算1+2+3+4+5——————————")
a = 1
total = 0
while a <= 5:
    total += a
    a += 1
print(total)
