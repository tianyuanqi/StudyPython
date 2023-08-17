def foo():
    print("mudule3模块的foo函数")
    pass


def bar():
    print("mudule3模块的bar函数")
    pass

# 执行代码最好放在如下所示的条件中
# __name__是Python中一个隐含的变量它代表了模块的名字
# 只有被Python解释器直接执行的模块的名字才是__main__
if __name__ == '__main__':
    print('call foo()')
    foo()
    print('call bar()')
    bar()