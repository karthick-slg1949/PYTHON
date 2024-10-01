from  abc import *

class Bank(ABC):

    @abstractmethod
    def cal_tax(self):
        pass
b=Bank()
print(id(b))