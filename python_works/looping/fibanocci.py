range=int(input("enter the range:"))

start=1

prev=0
current=1

print(prev,end=" ")
print(current,end=" ")

while(start<=range):
    sum=prev+current
    print(sum,end=" ")
    prev=current
    current=sum
    # (prev,current)=(current,sum)
    start+=1

# num find the num is present there in fibanocci