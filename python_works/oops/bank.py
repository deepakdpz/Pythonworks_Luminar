from datetime import datetime

class Bank:

    bank_name:str
    acno:str
    person_name:str
    ac_type:str
    balance:int

    def create(self,b_name,acno,p_name,ac_type,bal):

        self.bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.balance=bal

    def deposit(self,amount):

        self.balance+=amount    
        print(f"your {self.bank_name} is credited with {amount} available balance is {self.balance}")
    
    def withdraw(self,amount):
        if self.balance<amount:
            print("transaction declined insufficient fund")

        else:
            self.balance-=amount
            print(f"your {self.bank_name} is debited with {amount} available balance is {self.balance}")
    
    def getbalance(self):
        print(f"your available balance on {datetime.today()} is {self.balance}")

obj1=Bank()
obj1.create("sbi","10345","vijay","savings",4000) 

# obj1.deposit(2000)
# obj1.withdraw(5000)
obj1.getbalance()

obj2=Bank()
obj2.create("sbi","103452","dhanush","current",3000)
