# 基础数据类型的注解


var1: int = 10
var2: str = "hello"
var3: bool = True


# 类对象类型的注解
class Student:
    pass


s1: Student = Student()

# 基础容器类型的注解

my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_dict: dict = {"money": 100}

# 容器类型的详细注解
my_list: list[int] = [1, 2, 3]
my_tuple: tuple[int,str,bool] = (1, "hello", False)
my_dict: dict[str,int] = {"money": 10}
print(my_dict)