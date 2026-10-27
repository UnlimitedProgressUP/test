import os
import time

print(f"当前进程的pid是：{os.getpid()}")  # os.getpid() 获取进程号的
print(f"当前进程的父进程pid是：{os.getppid()}")
time.sleep(10)
