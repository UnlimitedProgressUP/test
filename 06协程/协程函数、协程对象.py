import asyncio         # 实现协程要引入asyncio

# 协程是一种可以被挂起，并在挂起后，还可以恢复执行的函数
# 有I/O 操作的挂在一边  让不是的先执行  协程不是操作系统提供的 ，而是程序员在用户态，实现的一种切换机制

# 协程函数  使用 async的关键字修饰的函数 ，就是协程函数
# 协程对象  调用协程函数，就会得到协程对象
#  调用协程函数，并不会执行协程函数中的代码

async def work():
    print("执行开始")
    print("执行中....")
    print("执行结束")
    return "Hello"
# 调用协程函数，就会得到协程对象
result = work()
res=asyncio.run(result)    #执行这个方法run() 执行协程函数 要把协程对象放进去  res  接收return的返回值
print(res)

# asyncio.run 方法做了3件事
# 1 创建一个事件循环
# 2 将收到的协程对象，包装成一个任务 (task),交给事件循环
# 3 启动事件循环
# 注意 asyncio.run 会阻塞当前线程， 直到任务执行完毕，并返回该任务 return的最终结果