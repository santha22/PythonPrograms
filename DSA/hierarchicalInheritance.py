class Parent:
    def fun1(self):
        print("this is parent class")

class Child1(Parent):
    def fun2(self):
        print("this is child class")

class Child2(Parent):
    def fun3(self):
        print("this is Grandchild class")


obj = Child1()
obj.fun1()
obj.fun2()