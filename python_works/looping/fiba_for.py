count=int(input("enter the range:"))

prev=0
current=1

print(prev,end=" ")
print(current,end=" ")

for i in range(1,count+1):
    sum=prev+current
    prev=current
    current=sum
    if(sum<=count):
        print(sum,end=" ")
        
    else:
        break
    

