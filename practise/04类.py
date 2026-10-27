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
# 供实例调用
    def speak(self, msg):
        print(f"我叫{self.name},年龄是{self.age},我想说{msg}")
    @classmethod  # 类方法 
    def test1(cls):
        print("test1")

     # 创建Person类的实例对象
p1=Person("王五",98)    # 这里要传数字 ，而不是字符

# p2=Person("李白","18")
# print(p1.__dict__)      # 可以查看实例身上的所有属性
p1.address="北京市"
# print(p1.address)

# 自定义方法   self 实例化对象
p1.speak("我肯定可以") # 实例化对象调用方法
# p2.speak("没事逗逗女孩")

# 类的属性
# print(Person.max_age)
# print(p1.planet)