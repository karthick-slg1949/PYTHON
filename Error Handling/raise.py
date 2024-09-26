class InsufficientBalError(Exception):
    def __init__(self,msg):
        self.msg=msg
def Withdraw():
    amount=int(input("Enter the withdrawl Amoount:"))
    acc_bal=6000
    if acc_bal>amount:
        print("Withdrawl and enjoy")
    else:
        raise InsufficientBalError("low balance")
Withdraw()