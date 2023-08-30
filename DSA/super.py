class A:
    def __init__(self):
        print("this is class a")

    def fun1(self):
        print("this is Father class")

class B(A):
    def __init__(self):
        print("this is class b")
        super().__init__()

    def fun2(self):
        print("this is Mother class")

obj = B()