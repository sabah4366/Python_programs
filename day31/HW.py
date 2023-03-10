class BankAccount:
    def __init__(self):
        print(f"1:New customer\n2:Deposit\n3:Withdrawal\n4:display\n5:exit")
        bankname='FEDERAL BANK'

    def newcustomer(self):
        self.name=input("enter your name")
        self.acnumber=int(input("enter the account number"))
        self.acctype=input("enter the type of account")
        self.blnc=int(input("enter the amount  "))
    def deposit(self):
        dpstamount=int(input("enter the amount to be deposited"))
        self.blnc = self.blnc + dpstamount
        print("current balnce", self.blnc)

    def withdrawal(self):
        wthdrw=int(input("enter the amount to be withraw"))
        if wthdrw>self.blnc:
            print("insufficient balance\ncurrent balance:",self.blnc)
        else:
            self.blnc=self.blnc-wthdrw
            print("current balance", self.blnc)


    def details(self):
        print(f"{self.name}\n{self.acnumber}\n{self.acctype}\n{self.blnc}")
    def exit(self):
        print("PROGRAM TERMINATED")



obj=BankAccount()
while True:
    choice=int(input("enter your choice"))
    if choice==1:
        obj.newcustomer()
    elif choice==2:
        obj.deposit()
    elif choice==3:
        obj.withdrawal()
    elif choice==4:
        obj.details()
    elif choice==5:
        obj.exit()
        break
    else:
        print("invalid choice")
        break

'''
#this is another method


class Account:
    def __init__(self):
        print(f"1:New customer\n2:Deposit\n3:Withdrawal\n4:display\n5:exit")

    def main(self):
        choice=int(input("enter your choice"))
        self.balanceamount=1000
        if choice==1:
            self.name = input("enter your name")
            self.acnumber = int(input("enter the account number"))
            self.acctype = input("enter the type of account")
            print("balance amount", self.balanceamount)


        elif choice==2:
            dpstamount = int(input("enter the amount to be deposited"))
            self.balanceamount=self.balanceamount+dpstamount
            print("balance amount", self.balanceamount)

        elif choice==3:
            wthdrw = int(input("enter the amount to be withdraw"))
            if wthdrw>self.balanceamount:
                print("insufficient fund\nyour current balance:",self.balanceamount)
            else:
                self.balanceamount=self.balanceamount-wthdrw
                print("balance amount", self.balanceamount)



        elif choice==4:
            print("PROGRAM TERMINATED")
        else:
            print("invalid choice")

A1=Account()
A1.main()
'''
