class Animal:
    def speak(self):  # 抽象方法，没有方法体，交给子类去实现
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")  # 子类实现了父类的抽象方法


class Cat(Animal):
    def speak(self):
        print("喵喵喵")  # 子类实现了父类的抽象方法


def make_noise(animal: Animal):
    animal.speak()
    pass


dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)
