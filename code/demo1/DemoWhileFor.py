a = 10
while a > 0:
    print(a)
    a-=1
    if a == 3:
        break

b = 10
for i in range(b):
    if i > 5:
        continue
    print(i)