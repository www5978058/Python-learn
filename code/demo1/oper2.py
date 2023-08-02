"""
关系运算符,结果均为bool
> < >= <= == != is is not
python字符串比较大小是从第一位开始比较ASSIC码
python可以使用双判断 c<a<b
"""
a = 1
b = 2
print(a > b)
print(a < b)
print(a == b)
print(a is not b)
c = 3
print(a < b < c)
print(b < a < c)
