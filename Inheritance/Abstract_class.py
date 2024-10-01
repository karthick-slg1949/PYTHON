from abc import *

class Bank(ABC):
    def cal_tax(self):
        pass
b=Bank()
print(id(b))