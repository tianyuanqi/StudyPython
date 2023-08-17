
class Phone:
    __current_voltage=3.3 #当前电压，这是一个私有成员

    def __power_save_model(self): #私有方法，用来开启省电模式
        print("开启省电模式")

    def call_by_5g(self): #定义一个方法，用来开启手机的5g功能
        if self.__current_voltage >= 3.6:
            print("开启5g")
        else:
            self.__power_save_model()
            print("电量不足，无法开启5g，并且已经切换到省电模式")
phone = Phone()
print(phone.__current_voltage) #
phone.call_by_5g()

