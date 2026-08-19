count = 1

# 要求1:遇到3，6时使用continue

while count <= 10:
    if count == 3 or count == 6:
        count += 1
        continue
    else:
        print(count)
        count += 1

print("——————————————————分割线————————————————————")
attempt = 1

while attempt <= 5:
    print(f"第{attempt}次尝试")
    if attempt == 3:
        print("操作成功")
        break
    else:
        attempt += 1

# Q: break 和 continue 的区别是什么？
# A: break是结束整个循环，continue只是跳出当前循环，开始下一次循环

# Q: while 最容易出现什么问题？
# A: 容易出现死循环

# Q: 如何避免 while 死循环？
# A: 可以定义一个最大执行次数，达到最大执行次数之后直接break结束整个循环