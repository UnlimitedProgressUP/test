# python 操作文件的标准流程
# 1创建 【文件对象】   open 有打开 、创建
# 2 操作文件 (读取、写入)
# 3 关闭文件
# open 函数 常用的参数3个 如下：它可以打开或者创建文件 且支持多种操作模式 返回值是文件对象

    #   1 file 要操作的文件路径
    #   2 mode 文件的打开模式
    # r 读取   (默认模式)
    # w 写入, 并先截断文件
    # a打开文件用于写入 文件存在在文件尾部追加内容
    # t文本模式  (默认模式)
    # x 排他性创建 如果文件已存在、则创建失败
    #    3 encoding 字符编码

# 1 创建文件 对象
# file =open(file="test.txt",mode="r",encoding="utf-8") # file 变量  括号里是参数

# file =open(file="test.txt",mode="r")
# # 操作文件方法 (读取)
# re=file.read()
# print(re)
# #关闭文件
# file.close() # 不关闭内存会占这 ，也会占用文件

with open('test.txt', 'rt',encoding='utf-8') as file:   # open 所有参数交给file 变量
    result = file.read()
    print(result)