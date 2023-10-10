class Employee:

    id:int
    name:str
    gender:str
    department:str
    experience_yr:int

    def create(self,id,name,gender,dept,exp):

        self.id=id
        self.name=name
        self.gender=gender
        self.department=dept
        self.experience_yr=exp

    def display_details(self):

        print(self.id,self.name,self.gender,self.department)    

    def __str__(self):

        return self.name

emp1=Employee()

emp1.create(100,"deepak","male","hardware",5)

emp1.display_details()

print(emp1)