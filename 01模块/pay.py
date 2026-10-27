# 支付超时时间
timeout = 1000
# 微信支付
def wechat_pay():
    print("我是微信支付")
#支付宝支付
def ali_pay():
    print("我是支付宝支付！")
#提示函数
def show_order():
    print("我是来自支付宝模块的提示")

if __name__ == "__main__":  # 说明我现在的身份是被直接运行的主程序
    ali_pay()