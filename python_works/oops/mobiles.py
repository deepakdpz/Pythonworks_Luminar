class Mobiles:

    brand:str
    model:str
    colour:str
    price:int

    def __init__(self,brand,model,colour,price):

        self.brand=brand
        self.model=model
        self.colour=colour
        self.price=price

    def display(self):

        print(self.brand,self.model,self.colour,self.price)


mobile1=Mobiles("redmi","note 11","black",14500)

mobile1.display()