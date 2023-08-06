"""
list.append()
list1+list2
list.pop(index) 不填默认最后一个 超出下标或列表为空报错
list.remove(item)  元素不存在报错
list.insert(index,item) 往指定位置添加
clear() 清空
"""
list = ["zs","ls","ww"]
list.append("zl")
print(list)
list2 = ["zz"]
list += list2
print(list)
print(list.pop())
print(list)
print(list.pop(2))
print(list)
list.remove("ls")
print(list)