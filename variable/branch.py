'''
迄今为止，我们写的Python代码都是一条一条语句顺序执行，这种代码结构通常称之为顺序结构。
然而仅有顺序结构并不能解决所有的问题，比如我们设计一个游戏，游戏第一关的通关条件是玩家获得1000分，
那么在完成本局游戏后，我们要根据玩家得到分数来决定究竟是进入第二关，还是告诉玩家“Game Over”，
这里就会产生两个分支，而且这两个分支只有一个会被执行。类似的场景还有很多，我们将这种结构称之为“分支结构”或“选择结构”。

在Python中，要构造分支结构可以使用`if`、`elif`和`else`关键字，这里举了一个很典型的例子来构造一个分支结构
        username = input('请输入用户名: ')
        password = input('请输入口令: ')
        # 用户名是admin且密码是123456则身份验证成功否则身份验证失败
        if username == 'admin' and password == '123456':
            print('身份验证成功!')
        else:
            print('身份验证失败!')
'''



##英寸和厘米的转换
value = float(input("请输入长度:"))
unit = input("请输入单位:")
if unit == 'in' or unit == "英寸":
    print('%f英寸等于%f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == "厘米":
    print('%f厘米等于%f英寸' % (value, value / 2.54))
else:
    print("请输入有效的单位")

## 百分制成绩转换为等级制成绩
## 要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E
score = float(input("请输入学生成绩"))

if score >= 90 :
    grade = 'A'
elif score >=80 :
    grade = 'B'
elif score >=70 :
    grade = 'C'
elif score >=60 :
    grade = 'D'
else:
    grade = 'E'
print("该学生的成绩为:",grade )





## 输入三条边长，如果能构成三角形就计算周长和面积
a = float(input("请输入第一条边a："))
b = float(input("请输入第二条边b："))
c = float(input("请输入第三条边c："))

if a + b > c and a + c > b and b + c > a:
    print('三角形的周长为%f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('三角形的面积为：%f' % (area))
else:
    print("不能构成三角形")

