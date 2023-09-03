"""
格式：
def 函数名(参数):
    代码
"""


# 无参
def func():
    pass


# 多参
def sum(a, b):
    return a + b


# 默认参必须放最后
def sum2(a, b=5):
    return a + b


# 多默认参调用

def func2(a, b=1, c=3):
    print(a, b, c)


func2(1, c=10)
