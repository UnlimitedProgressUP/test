#生成器函数：函数体如果出现yield 关键字 该函数是生成器函数
#生成器对象：调用生成器函数时，其函数体不会立刻执行 而是返回一个生成器对象

def demo():        # 生成器函数
    print("demo函数开始执行")
    print(100)
    yield  "返回1 " # 不写就是None
    a=200
    print(a)
    b=300
    print(b)
    return "ok"

#region
d=demo() # d 接住 返回值  返回生成器对象
# print(d) # generator     执行调用next方法
# 1 调用生成器对象的 __next__方法，会让生成器函数中的代码开始执行
# 2 用生成器函数中的代码开始执行后， 遇到yield 会暂停执行 并且其内部会记录 "暂停" 位置
# d.__next__()
result=next(d)
print(result)  # 返回1
result2=next(d)
print(result2)
try:
    next(d)
except StopIteration as e:
    print(e)
#endregion

