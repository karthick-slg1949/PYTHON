class Account():
    def __init__(self,id,name,amount):
        self.acc_id=id
        self.acc_name=name
        self.acc_bal=amount
    def deposit_amount(self,amount):
        self.acc_bal=self.acc_bal+amount
a1=Account(101,"karthick",89000)
a1.deposit_amount(100000)
a1.deposit_amount(90000)
a2=Account(102,"satheesh",78888)
a2.deposit_amount(788888)
a3=Account(103,"dinesh",90000)
a3.deposit_amount(6777777)

print(a1.__dict__)
print(a2.__dict__)
print(a3.__dict__)