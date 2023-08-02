"""
字符串查询内容使用find index rfind rindex count方法
find 返回第一个符合的下标，没有返回-1
rfind 右侧开始找，返回第一个符合的下标，没有返回-1
index和find区别: index找不到会报错
count 查询指定字符串数量
"""
str = "abcdefc"
print(str.find("c"))
print(str.rfind("c"))
print(str.index("c"))
print(str.rindex("c"))
print(str.count("a"))
"""
2
6
2
6
"""