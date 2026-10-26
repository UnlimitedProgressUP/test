class Person:   # 类属性 可以通过类访问，也可以通过实例访问  保存公共数据
    max_age=88
    planet="地球"

    def __init__(self,name,age):
        # 实例.属性名 = 值  给实例添加属性  叫 实例属性
        self.name=name

        if age<= Person.max_age:
            self.age=age
        else:
            print(f"年龄超过了最大值,将年龄设为最大值{Person.max_age}")
            self.age= Person.max_age
# 供实例调用  实例化方法
    def speak(self, msg):
        print(f"我叫{self.name},年龄是{self.age},我想说{msg}")

# 类方法保存在类身上  类方法可以访问类属性
    @classmethod  # 类方法
    def test1(cls):  # 形参是cls  # <class '__main__.Person'>   cls是当前的类
        print("test1",cls )
        print(Person.planet)

     # 创建Person类的实例对象
p1=Person("王五",18)
p1.speak("我肯定可以")

# 类方法调用
Person.test1()