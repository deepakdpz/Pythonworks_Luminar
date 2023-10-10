class Bike:

    def starting(self):
        print("kicker start")

    def braking(self):
        print("drum brake")

class HeroHondaSplendor(Bike):      

    def starting(self):
        print("self start")   

    def braking(self):
        print("abs braking")       

ob=HeroHondaSplendor()

ob.starting()
ob.braking()