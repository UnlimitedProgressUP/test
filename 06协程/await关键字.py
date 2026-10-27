import asyncio
async def work():
    print("work开始")
    print("work执行中")
    res= await asyncio.sleep(2)
    print("work结束")
    return '工作结果'

async def main():
    print("main开始")
    # await 去等待一个协程对象(靠自己去编写协程函数，随后调用该函数来得到协程对象)
    res =await work()  # 调用他会返回来过 1个 return 一个值
    print(res)  # work return 返回来的
    print("main结束")
    return 'main的返回值'

result = asyncio.run(main())
print(result)