def generate_cases():
    print("准备case01")
    yield "case01"

    print("准备case02")
    yield "case02"

    print("准备case03")
    yield "case03"


cases = generate_cases()
print(type(cases))  # class generator

print(next(cases))  # 准备case01
print(next(cases))  # 准备case02
print(next(cases))  # 准备case03
try:
    print(next(cases))
except StopIteration:
    print("所有测试用例已经生成完毕")

cases = generate_cases()

for case in cases:
    print(f"执行{case}")

# Q1:
# 调用 generate_cases()
# 会直接执行完整个函数吗？
# A: 不会,generate_cases()是返回一个生成器对象，生成器是按需调用


# Q2:
# yield 和 return
# 在函数执行行为上的主要区别是什么？
# A: retun是自己定义返回的数据和类型，执行到return之后函数就会结束，
# yield会产生一个值并暂停函数，同时保留当前的执行状态，下一次调用next()时候会从之前的状态继续执行
# 调用包含yield的生成器函数时，返回的是生成器对象


# Q3:
# 第一次 next(cases)
# 执行到哪里会暂停？
# A: 执行到yield "case01"就会暂停


# Q4:
# 第二次 next(cases)
# 是从函数开头重新执行吗？
# A:不是，是从准备case02开始执行


# Q5:
# 为什么生成器可以直接放进for循环？
# A: 因为生成器就是迭代器，for就是用来循环从迭代器里面取数据的