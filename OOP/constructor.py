class Test:
    def __init__(self):
        print("Test class - Constructor Method")
    def m1(self):
        print("Test class - Iinitialize Method")
    @classmethod
    def m2(cls):
        print("Test class - class method")
    @staticmethod
    def m3():
        print("Test class - Static method")

t1=Test()
t2=Test()
t1.m1()
t1.m1()