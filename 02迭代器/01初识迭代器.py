# 能被for 循环遍历的对象 被称为可迭代对象 (iterbale)
#region
# name =["李白","白居易",'黄巢']
# citys=("北京",'上海','深圳')
# msg = 'Hello'
# res=10
# for item in citys:  # citys 迭代器
#     print(item)
#endregion

#region
# #  调用__iter__ 方法会得到 迭代器 iterator
# name =["李白","白居易",'黄巢']
# citys=("北京",'上海','深圳')
# msg1 = 'Hello'
# # print(name.__iter__())
# # print(msg1.__iter__())
#
# # __iter__是一个魔法方法   当调用iter函数时 __iter__会自动调用    等价于 iter(可迭代对象 )
# print(iter(name))       # <list_iterator object at 0x000001DBFBDB1780>
# #迭代器(iterator)拥有__next__方法 每次调用都会根据当前的状态，返回下一个元素
# # 迭代器.__next__() 等价于 next(迭代器)
# name =["李白","白居易",'黄巢']
# it=iter(name)
# print(next(it))   # 没nexte 1次 指针就会往后面指 1次
# print(next(it))
# print(next(it))
# #endregion

name1 =["李白","白居易",'黄巢']
citys1=("北京",'上海','深圳')
msg2 = 'Hello'