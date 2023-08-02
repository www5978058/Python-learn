"""
算数运算符
+ - * / // ** %
"""
print(1+2) #3
print(5-2) #3
print(1*3) #3
print(6/2) #3.0
print(6//2) #3
print(3**1) #3
print(8%5)

# 打印三位数123的个十百位数
num = 123
print("%s的个位数为%s" % (num,num % 10))
print("%s的十位数为%s" % (num,num // 10 % 10))
print("%s的百位数为%s" % (num,num // 100))