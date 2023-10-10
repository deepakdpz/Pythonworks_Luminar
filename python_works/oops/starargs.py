
# def add(*args):
#     return sum(args)


# print(add(10,20))


# def product(*args):
#     res=1
#     for i in args:
#         res*=i
#     print(res)

# product(1,2,3)        


#--------------------------------------------

# def display_emp(**kwargs):
#     print(kwargs)
#     print(kwargs.get("name"))

# display_emp(name="arjun",dept="hr",place="tvm",salary=24000) 

#-------------------------------------------------------------------


def display_student(**kwargs):
    print(kwargs.get("name"))
    print(kwargs.get("course"))

display_student(name="ravi",course="django",roll=1000,gender="male")    