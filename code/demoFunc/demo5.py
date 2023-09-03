def test(func):
    def wapper(*args, **kwargs):
        print("start")
        res = func(*args, **kwargs)
        print("end")
        return res
    return wapper


@test
def learn(name):
    print(name + "学习中")
    return True


res = learn("zs")
print(res)