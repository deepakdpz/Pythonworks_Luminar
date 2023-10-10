# class Parent:

#     def phone(self):
#         print("redmi note 11")

#     def bike(self):
#         print("splendor")    

# class Child(Parent):

#     def phone(self):
#         print("i phone")        

# ob=Child()

# ob.phone()
# ob.bike()

class Parent:

    vehicles=["passionpro","swift"]

    def vehicle(self):

        return self.vehicles
    
class Child(Parent):

    def vehicle(self):

        
        self.veh=super().vehicle()

        self.veh.append("hunter")
        
        return self.veh 


ch=Child()

print(ch.vehicle())
