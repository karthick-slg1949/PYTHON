'''
Account holder details
acc_bal
min_bal
branch_name
'''

class Account:
    def open_account(self):
        print('Account open successfully')
    def deposite(self):
        print('Amount deposited')
    def withdrawl(self):
        print('Amount withdrawl!')
    def get_bal(self):
        print('Low Bal')

a1=Account()
a1.open_account()
a1.deposite()
a1.withdrawl()
a1.get_bal()