"""
字符串替换 replace(old,new,count)
字符串切割split,rsplit,
"""

str = " hello hello world "
newStr = str.replace("hello","say")
print(newStr)
print(str.replace("hello","say",1))
print(str.split(" "))
print(str.split(" ",1))
print(str.rsplit(" ",1))
str2 = """aaa
bbb
"""
print(str2.splitlines())
print(str.title())
print(str.upper())
print("{}在{}".format("zs","cs"))
