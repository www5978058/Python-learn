def sum(*args):
    print(args, type(args))
    res = 0
    for i in args:
        res += i
    return res


res = sum(1, 2, 3)
print(res)
a, *b = 1, 2, 3, 4
print(sum(*b))


def func(**kwargs):
    print(kwargs.get("aaa"))


func(aaa=1, bbb=2)
func(**{"aaa": 12})
