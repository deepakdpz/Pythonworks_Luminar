num=1634

temp=num

sum=0

while(num!=0):
    r=num%10
    cube=r**4
    sum=sum+cube
    num//=10

if(temp==sum):
    print(f"{temp} is an armstrong number")

else:
    print(f"{temp} is not an armstrong number")        