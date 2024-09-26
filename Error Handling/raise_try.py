class InsuffientBalError(Exception):
    def _init_(self,msg):
        self.msg=msg

def withdrawl():
    try:
        amount = int(input("Enter Amout to withdrawl:"))
        acc_bal  = 5000
        if acc_bal > amount:
            print("Withdrawl and enjoy")
        else:
            raise InsuffientBalError("Low Bal")
    except InsuffientBalError as err:
        print(err.msg)

withdrawl()
print("Good Morning")