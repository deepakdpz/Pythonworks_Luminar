from abc import ABC,abstractmethod




class Banking(ABC):

    @abstractmethod
    def fund_transfer(self):
        pass


    @abstractmethod
    def balance_check(self):
        pass 


    @abstractmethod
    def transaction_history(self):
        pass


class Paytm(Banking):

    def fund_transfer(self):
        print("amount is transferred succesfully")


    def balance_check(self):
        print("your balannce is")


    def transaction_history(self):
        print("your history")   


obj=Paytm()

obj.fund_transfer()