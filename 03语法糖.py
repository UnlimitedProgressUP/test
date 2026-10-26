
  # check_login   装饰器名
def check_login(fn_name): # fn_name 要被装饰的函数名   comment /payment
    def fn_inner():      #有嵌套
        print("校验登录..登录成功")                          #原函数调用之前   增加额外功能
        fn_name()        #  原函数  访问原函数 有  ()
        print("原函数调用之后") # 增加额外功能
    return fn_inner


def comment():
    print("发表评论")
@check_login
def payment():
    print("充值中")


#     # 装饰后的函数名 = 装饰器名(被装饰的原函数名)
#     # 装饰后的函数名()

payment()  # 装饰语法糖  调用函数

# 调用
# abc = check_login(comment)  # return fn_name       abc保存了 fn_inner 的函数
#
# abc()                   # abc 就是comment      ( 装饰的函数 )
# # comment()             #    也可以这样写