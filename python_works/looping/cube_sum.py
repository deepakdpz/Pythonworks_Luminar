num=153

temp=num

sum=0

while(num!=0):
    last_digit=num%10
    cube=last_digit**3
    sum=sum+cube
    num//=10

if(temp==sum):
    print(f"{temp} is an armstrong number ")
else:
    print(f"{temp} is not an armstrong number")    