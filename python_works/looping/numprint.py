start=1
end=50

# print number from 1 to 50 if num/3 a if num/5 cd if num/15 efg else print num

while(start<=end):
    if(start%15==0):
        print("efg")
    elif(start%5==0):
        print("cd")
    elif(start%3==0):
        print("a")
    else:
        print(start)
    start+=1                