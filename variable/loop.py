'''
循环结构
python有两种循环结构，for-in循环和while循环
'''

'''
for-in循环
如果明确的知道循环执行的次数，或者对某个容器进行迭代，使用for-in循环
'''

# 求1-100的和
sum = 0
for x in range(101):
    sum += x
print(sum)

# range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
# range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
# range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。

# 求1-100以内偶数的和
sum = 0
for x in range(2, 101, 2):
    sum += x
print(sum)

'''
while循环
如果不知道循环次数，则用while循环会比较合适
'''
import random

result = random.randint(1, 100)
count = 0
while True:
    count += 1
    answer = int(input("请输入数字"))
    if answer > result:
        print("猜错了，偏大了点儿")
    elif answer < result:
        print("猜错了，偏小了点儿")
    else:
        print("恭喜你猜对了，共猜了%d次" % count)
        break

##打印三角形
'''
*
**
***
****
*****
'''
row = int(input("请输入行数"))
for i in range(row):
    for _ in range(i + 1):
        print("*", end='')
    print()

##打印三角形
'''
    *
   **
  ***
 ****
*****
'''
row = int(input("请输入行数"))

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(" ",end='')
        else:
            print("*",end='')
    print()



