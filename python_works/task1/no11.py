people=int(input("number of people you want to invite:"))

if people<10:
   
    for i in range(1,people+1):
       
        name=input("enter the person name:")
       
        print(f"{name} has been invited")

elif people>=10:
   
    print("Too many people")        