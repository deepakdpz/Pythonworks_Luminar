num=324

# output==>(3+2+4)

sum=0

while(num!=0):
    r=num%10
    sum=sum+r
    num//=10

print(sum)
     