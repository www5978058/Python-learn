
def test(func):
    def wapper():
        print("start")
        func()
        print("end")
    return wapper

@test
def learn():
    print("学习中")

learn()