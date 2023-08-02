"""
进制转换 十进制转二、八、十六进制，使用bin()、oct()、hex()方法
0b 二进制 0o八进制 0x 十六进制
"""
a = 100
print(bin(a)) # 0b1100100
print(oct(a)) # 0o144
print(hex(a)) # 0x64
print(type(hex(a)))
print(int(0b1100100))
print(type(int(0x64)))