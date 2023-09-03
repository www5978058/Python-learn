dict = {'name': "zs", 'age': 10,"gender": '男'}
# dict["aaa"],key不存在报keyError错误 get方法不报错，可以返回默认值
print(dict.get("name")) #zs
print(dict.get("aaa")) #None
print(dict.get("aaa","bbb")) #bbb

for key in dict:
    print(key)

print(type(dict.keys()))
print(type(dict.values()))
for key in dict.keys():
    print(key)

for tuple in dict.items():
    print(tuple)