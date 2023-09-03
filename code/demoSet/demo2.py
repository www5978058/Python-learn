set = set(range(10))
print(set)
# remove元素不存在报错keyError
set.remove(5)

print(set)
# discard元素不存在不报错
set.discard(8)
set.discard(11)
print(set)
# 随机删除
set.pop()
print(set)

