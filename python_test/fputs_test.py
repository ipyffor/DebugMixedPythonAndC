# fputs_test.py

import os

# 打印当前进程id
print("pid:",os.getpid())

# 调用模块
import fputs


fputs.fputs("hello world! You are good!", "hello.txt")

print("hello world!")