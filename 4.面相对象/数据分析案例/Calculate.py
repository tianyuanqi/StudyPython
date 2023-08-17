


from ReadFile import ReadFile, TextFileReader,JsonFileReader
from Data_define import Record


#1.读取两份文件，组成一份新的数据并保存在List中
#2.定义一个字典类型的数据来保存计算结果
# 数据格式 {"2011-02-01":1689,"2011-02-03":2291}，key来存储日期，value来保存

list1 = TextFileReader("/Users/yuanqi/PycharmProjects/StudyPython/4.面相对象/数据分析案例/test/2011.txt").read_data()
list2 = JsonFileReader("/Users/yuanqi/PycharmProjects/StudyPython/4.面相对象/数据分析案例/test/2011-2.txt").read_data()

data : list[Record] = list1+list2
result ={}
# for i in  data:
#     print(i)

for i in data:
    if i.date in result.keys():
        result[i.date] += i.money
    else:
        result[i.date] =i.money

print(result)