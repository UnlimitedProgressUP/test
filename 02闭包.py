def fun():
    a=3
    def ga():            #内部函数 g
        nonlocal a     #nonlocal 声明a 不是ga自己的，而是 外面fun函数的
        a+=1           #把外面的 a+1
        print(a)
    return ga        # f函数把内部函数g作为结果 ，交给了外面

res=fun()   #调用f()  return ga 把 ga函数交出来  res 保存ga函数             a=3打包塞进 ga的背包一起交给res
res()     # res() = ga()      于是跳进 ga 函数内部：a 变成 4，打印出 4。执行完毕
res()
print("-" *23)



def outer(num1):
     #1 定义内部函数
    def inner(num2):
        #2 求和
        sum=num1+num2
        print(sum)
    return inner  # 3 返回


ad= outer(10)   # ad =inner  num1=10     之前 ad 是变量，返回 inner 之后 ad 变成了 inner
ad(20)  # 有一次调用了 inner num1=10  num2=20
ad(30)  #10+30