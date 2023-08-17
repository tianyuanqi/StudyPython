import json

from Data_define import Record

class ReadFile:

    def __init__(self,path):
        self.path=path
        pass

    def read_data(self):
        pass

class TextFileReader(ReadFile):
    def read_data(self) -> list[Record]:
        read=open(self.path,"r",encoding="utf-8")
        listRecord: list[Record]=[]
        for line in read.readlines():
            line=line.strip()
            datelist=line.split(",") #使用split方法将字符串切分成存放字符串的数组，再根据数组下标填充进Record对象中
            record=Record(datelist[0],datelist[1],int(datelist[2]),datelist[3])
            listRecord.append(record)
        read.close()
        return listRecord

class JsonFileReader(ReadFile):
    def read_data(self) -> list[Record]:
        read=open(self.path,"r",encoding="utf-8")
        listRecord: list[Record]=[]
        for line in read.readlines():
            data_dict=json.loads(line) #使用json.load方法读取内容，并转换为dict对象
            record=Record(data_dict["date"],data_dict["order_id"],data_dict["money"],data_dict["province"])
            listRecord.append(record)
        read.close()
        return listRecord

if __name__ == '__main__':
    textFileReader=TextFileReader("/Users/yuanqi/PycharmProjects/StudyPython/4.面相对象/数据分析案例/test/2011.txt")
    result=textFileReader.read_data()

    jsonFileReader=JsonFileReader("/Users/yuanqi/PycharmProjects/StudyPython/4.面相对象/数据分析案例/test/2011-2.txt")
    result2 =jsonFileReader.read_data()

    for i in result:
        print(i)

    print("————————————————————————分割线——————————————————————————")
    for i in result2:
        print(i)
