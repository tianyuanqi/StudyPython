
#range的作用是生成一个指定范围的整数序列。常用于循环结构中，特别是for循环，常使用range函数来遍历数据
print()
'''
range的语法格式：
语法1:range(num)
语法2:range(num1,num2)
语法3:range(num1,num2,step)
'''

'''
range注意事项
语法1从0开始，到num结束（不包含num本身）
语法2从num1开始，到num2结束（不包含num2本身）
语法3从num1开始，到num2结束（不包含num2本身），步长为step
'''

#语法1，输出5次hello语句
for i in range(5):
    print("hello")

#语法2,求1到100的和
sum=0
for i in range(1,101):
    sum+=i
print(sum)

#语法3，打印10以内的奇数
for i in range(1,10,2):
    print(i)