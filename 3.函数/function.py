
'''
函数是一段可以重复使用的代码块，它可以接受参数并执行指定的任务，然后返回一个结果
函数的作用是组织和重复利用代码，提高代码的可读性和可维护性
'''
print("-----------------------------1.定义一个函数---------------------------------------")
#统计字符串长度
str1="fsdfhdfew"
str2="fffffhdfew"
str3="fsdffffffhdfew"

def count_str(str):
    count=0
    for i in str:
        count+=1
    print("字符串的长度为:",count)

count_str(str1)
count_str(str2)
count_str(str3)
'''
说明：
这里定义了一个函数count_str(str),它可以接收一个字符串作为传参
函数内部采用了for循环来遍历字符串，使用count来进行计数，每访问到一个字符，count会+1
在遍历完成以后，count的值就是该字符串的长度
后面执行了三次count_str(str)3.函数，分别传入了str1,str2,str3三个字符串，最终会打印它们三个字符串的长度
'''

print("--------------------2.函数的特性，同一个文件中两个同名函数，后面的会对前面的进行覆盖-------------------------------------")

#python是不存在"函数重载"这个概念的
#如果在同一个文件中定义了两个名字一样的函数，后面定义的函数会对前面定义的函数进行一个覆盖
def foo():
    print('hello, world!')

def foo(str):
    print(str)

#foo() #如果执行该条语句，会出现类型错误TypeError: foo() missing 1 required positional argument: 'str'
foo("hello") #执行后面定义的foo函数，这条语句能够正常执行

'''
说明，在这一段代码中，先后定义了两个函数foo，但由于python并不存在函数重载，导致第二个函数foo(str)对第一个函数foo()进行了覆盖
所以这段程序中只存在一个函数foo(str)，因此，在尝试调用第一个函数foo()时，会出现类型错误，会提示请求参数中少了一个传参
只有调用第二个函数foo(str)才可以正常执行
'''
print("--------------------------------2.使用模块来管理函数-----------------------------------------")

from module1 import foo
# 输出hello, world!
foo()

from module2 import foo
# 输出goodbye, world!
foo()

'''
在module1.py,和mudule2.py,两个文件中分别都定义了一个foo()方法，两个foo方法的返回结果是不相同的

'''

#也可以按照导入模块，然后起别名的方式，通过别名来调用指定的函数
import module1 as m1
import module2 as m2

m1.foo()
m2.foo()

#但是如果将代码写成了下面的样子，那么程序中调用的是最后导入的那个foo，因为后导入的foo覆盖了之前导入的foo。
from module1 import foo
from module2 import foo
# 输出goodbye, world!
foo()

# 需要说明的是，如果我们导入的模块除了定义函数之外还有可以执行代码，那么Python解释器在导入这个模块时就会执行这些代码，
# 事实上我们可能并不希望如此，因此如果我们在模块中编写了执行代码，最好是将这些执行代码放入如下所示的条件中，这样的话除非直接运行该模块，
# if条件下的这些代码是不会执行的，因为只有直接执行的模块的名字才是"__main__"。

import module3
module3.foo()

print("-------------------------分隔-----------------------------------------")

