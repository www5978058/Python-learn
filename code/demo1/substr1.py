"""
截取字符串  字符串变量[start:end],默认start为0,end默认为字符串长度
截取字符串  字符串变量[start:end:step],step为步长,-1为反着取
"""
str = "abcde"
print(str[1:2])
print(str[:3])
print(str[2:])
print(str[3::-1])