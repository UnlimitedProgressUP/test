class Person:   # 类属性 可以通过类访问，也可以通过实例访问  保存公共数据
    max_age=88
    planet="地球"

    def __init__(self,name,sex):
        # 实例.属性名 = 值  给实例添加属性  叫 实例属性
        self.name=name
        self.sex=sex
# 供实例调用  实例化方法
    def speak(self, msg):
        print(f"我叫{self.name},性别是{self.sex},我想说{msg}")

class Student(Person):  # 继承
    def __init__(self, name, sex, stu_id, grade):
        super().__init__(name,sex)       # 调用父类的属性   super().__init__
        # 子类独有的属性,需要自己手动完成初始化
        self.stu_id=stu_id               # student 独有的属性
        self.grade=grade

#方法重写 当子类定义一个与父类中相同的方法，那么子类中的方法就会 “覆盖”父类的方法
    def speak(self, msg):
        # super().speak("我一定可以成功")   super().speak(传参)   父类的speak方法      在子类前面调用
        print(f"我叫{self.name},我正在读{self.grade},我性别是:{self.sex}, 我想说{msg}")
        super().speak("我一定可以成功")    # 调用父类的speak方法  在子类的后面调用

s1=Student("李华","男","123456","初一")   # 也需要传 Person 类属性的值  如果传递多了，需要在自身定义初始化方法了
s1.speak("我肯定可以")  # 调用方法
