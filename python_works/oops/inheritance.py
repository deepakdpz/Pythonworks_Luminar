class Parent:

    phone="iphone15"
    vehicle="duke200"

    def mobile(self):
        print(self.phone)

    def bike(self):
        print(self.vehicle)

class Child(Parent):
    pass

obj=Child()

obj.mobile()
obj.bike()