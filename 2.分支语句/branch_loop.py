import math
import random

print()
'''
如果已知循环次数的话，可以使用for循环，例如对某个集合进行遍历
'''

# 用for循环实现1-100之和
sum = 0
for i in range(101):
    sum += i
print("1-100之和为:", sum)

# 求1-100的偶数和
sum = 0
for i in range(2, 101, 2):
    sum += i
print("1-100之间的偶数和为:", sum)

'''
如果不知道循环遍历的次数，可以使用while循环，
while通常用布尔值来控制循环，当表达式的值为true时，执行循环，当表达式为false时，终止循环
'''
# 猜数游戏，生成一个1-100之间的随机数，然后用户输入一个值去判断，如果玩家猜中了，输出共猜了多少次
def random_number():
    a = random.randint(1,100)
    count = 0
    while True:
        count += 1
        i = int(input("请输入一个值"))
        if i > a:
            print("猜错了，有点大，再试一次")
        if i < a:
            print("猜错了，有点小，再试一次")
        if i == a:
            print("恭喜你，猜对了，共猜了:",count,"次")
            break

#练习1：输入一个正整数判断是不是素数。
#提示：素数指的是只能被1和自身整除的大于1的整数。

def issushu():
    number=int(input("请输入一个正整数"))
    isPrime=True
    for i in range(2,int(math.sqrt(number)+1)):
        if number % i ==0:
            isPrime =False
            break
    if isPrime==True:
        print("该数是素数")
    else:
        print("该数不是素数")



#联系2：输入两个正整数，计算它们的最大公约数和最小公倍数。
#提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。

number1=int(input("请输入第一个正整数:"))
number2=int(input("请输入第二个正整数:"))


