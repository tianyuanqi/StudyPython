class phone:
    imei = 12345
    producer = "apple"

    def call_by_4g(self):
        print("使用4g网络")


class NFC:
    imei = 54321
    Card = "地铁卡"

    def user_NFC(self):
        print("使用NFC刷卡")


class iphone12(phone, NFC):
    producer = "苹果"  # 复写父类的成员属性
    face_id = True  # 面部识别功能,

    def call_by_5g(self):  # 子类的方法

        print(f"父类的厂商是：{super().producer}")  # 子类调用父类的属性
        print("使用5g网络")

    def call_by_4g(self):  # 复写父类的方法
        print("——————————————————————")
        print("增强了4g功能")
        super().call_by_4g()  # 子类调用父类的方法
        print("——————————————————————")


iphone12 = iphone12()
print(iphone12.producer)  # 子类重写了父类的producer属性，所以输出结果为子类重写后的内容，也就是"苹果"
print(iphone12.face_id)  # 子类拓展的属性，输出结果为True
iphone12.user_NFC()  # 子类继承了NFC这个父类，可以正常调用父类的方法
print(iphone12.imei)  # 由于是多继承，在定义子类时，左边的父类优先级高一些，所以imei属性继承自phone这个父类，也就是12345

iphone12.call_by_4g()  # 子类重写了父类的call_by_4g方法，所以调用的是子类重写后的方法，输出结果为"升级了配置，现在是4g增强网络"
iphone12.call_by_5g()  # 调用子类拓展的方法，这个方法中通过suer来访问了父类的属性
