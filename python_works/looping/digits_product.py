num=int(input("enter a number:"))

product=1

while(num!=0):
    r=num%10
    product=product*r
    num//=10

print(product)    
 