"""
union并集 difference差集 intersection交集
"""
set = {1,2,3}
set2 = {3,4,5}
print(set.union(set2))
print(set.intersection(set2))
print(set.difference(set2))
print(set)
print(set2)
print(set.difference_update(set2))
print(set)