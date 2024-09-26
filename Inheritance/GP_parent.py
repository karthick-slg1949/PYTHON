class GP:
    def m1(self):
        print("GP-class m1 method")
    def m2(self):
        print("GP - class m2 method")
class parent(GP):
    def m3(self):
        print("Parent - class m3 method")
class child(parent):
    def m4(self):
        print("Child - class m4 method")
obj=child()
obj.m1()
obj.m2()
obj.m3()
obj.m4()