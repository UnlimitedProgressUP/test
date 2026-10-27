
# nonlocal 声明让 内部函数 去 修改 外部函数的值

def outer():
    a=100
    def inner():
        nonlocal a
        a=a+1
        print(a)
    return inner    # 不带括号

func = outer()  # a =100保存在 背包里面
func()        # a=101
func()