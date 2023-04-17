
'''
将摄氏温度转换成华氏温度，公式：$C=(F - 32) \div 1.8$
'''

c=float(input('请输入摄氏温度'))
f=c*1.8+32
print(f)

'''
练习2：输入圆的半径计算计算周长和面积。
'''
r=float(input("请输入圆的半径"))
p=3.1415926
l=p*2*r
s=p*r*r
print("圆的周长为:",l,"面积为:",s)


'''
练习3：输入年份判断是不是闰年。
'''
year=int(input("请输入年份"))

if year %4 ==0 and year % 100 != 0 or year %400 ==0 :
    print("是闰年")
else:
    print("不是闰年")