class Parent:
    def fun1(self):
        print("this is parent class")

class Child(Parent):
    def fun2(self):
        print("this is child class")

obj = Child()
obj.fun2()
obj.fun1()