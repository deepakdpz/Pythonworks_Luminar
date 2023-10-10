class Student:
    
    id:int
    name:str
    age:str
    course=str

    def __init__(self,id,name,age,course):
        self.id=id
        self.name=name
        self.age=age
        self.course=course

    def display_student(self):

        print(self.id,self.name,self.age,self.course)


    def __str__(self):

        return self.name    


ob=Student(100,"deepak","23","python")

ob.display_student()
print(ob)