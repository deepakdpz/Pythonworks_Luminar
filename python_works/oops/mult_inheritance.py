class P1:

    def m1(self):
        print("inside p1 class m1 method")

class P2:

    def m2(self):
        print("inside p2 class m2 method")  

class Child(P1,P2):

    def m3(self):
        print("inside child class m3 method")


ch=Child()

ch.m3()
ch.m2()
ch.m1()



# name ambiguity error