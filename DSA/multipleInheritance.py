class Father:
    def fun1(self):
        print("this is Father class")

class Mother:
    def fun2(self):
        print("this is Mother class")

class Child(Father, Mother):
    def fun3(self):
        print("this is child class")


obj = Child()
obj.fun1()
obj.fun2()
obj.fun3()