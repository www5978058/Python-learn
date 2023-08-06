"""
sort() 没有返回值,默认升序，reverse=True 降序
reverse() 反转 无排序
"""
import random
list = []
for i in range(10):
    list.append(random.randint(1,20))
print(list)
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.reverse()
print(list)
