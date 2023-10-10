start=10
end=20

sum_evn=0
sum_odd=0

while(start<=end):
    if(start%2==0):
        sum_evn=sum_evn+start

    else:
        sum_odd=sum_odd+start
    start+=1

print(sum_evn)
print(sum_odd)            