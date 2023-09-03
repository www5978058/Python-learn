t1 = ()
t2 = 1,
print(type(t1))
print(type(t2))
t3 = 1, 2, 3
print(t3[2])
print(t3[1:2])
print(t3.index(2))
"""
3
(2,)
1
"""
t3 = 1, 2, 3
print(1 in t3)
for item in t3:
    print(item, end="\t")
print()

t3 = 1, 2, 3
l = list(t3)
l.append(4)
print(l)
print(tuple(l))