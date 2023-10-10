tummy_size=int(input("enter tummy size:"))
buttock_size=int(input("enter buttock size:"))
gender=input("enter M or F:")

measurement=tummy_size/buttock_size

val=round(measurement,2)

print(val)

if (gender=="M"):
    if(val<=0.95):
        print("health risk is low an body shape is pear")
    elif(val<1.0):
        print("health risk is moderate and body shape is avocado")
    else:
        print("health risk is high and body shape is apple")

elif(gender=="F"):
    if(val<=0.80):
        print("health risk is low an body shape is pear")
    elif(val<0.85):
        print("health risk is moderate and body shape is avocado")
    else:
        print("health risk is high and body shape is apple")

else:
    print("please enter a valid gender")
    


