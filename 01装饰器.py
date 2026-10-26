def outer(func):                     # func 是形参
    def inner(*args,**kwargs):              # inner 就是包好后的send
        #在执行原函数前触发
        #print("outer")
        value=func(*args,**kwargs)       #被装饰的  原函数  send (to,body) 自动*args  **kwargs 拆解开
        #在执行原函数后触发       这里执行send
        print("好好学")
        return value                        # return60 返回了但在这里没接收 value 就接受它
    return inner

@outer              # 2 执行outer这个函数 outer(send)  func就是原函数：send
def send(to,body):               # 把inner返回来 send 就变成 inner 了
    print("发微信",to,body)
# def write():
#     print("写字")
# def call():
#     print("打电话")
if __name__ == "__main__":
    res=send(1,2)     # 1 从这里开始执行
    print(res)       # 返回值  value

    # write()
    # call()
# 装饰器 、 参数 、返回值