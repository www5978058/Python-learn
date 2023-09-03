dict = {}
print(type(dict))
dict['name'] = 'zs'
dict['age'] = 18
dict['age'] = 20
dict[None] = 10
dict.setdefault("age",11)
print(dict)

dict = {'name': 'zs', 'age': 20, None: 10, True: False}
del dict['name']
print(dict)
# pop元素不存在时抛出KeyError异常
dict.pop('age')
print(dict)
# 删除最后一个元素
# popitem的字典为空时抛出KeyError异常
tuple = dict.popitem()
print(tuple)
print(dict)
dict.clear()
print(dict)