Lst=[10,11,10,11,12,13]

Lst.sort()

duplicate_lst=[]

limit=len(Lst)-1

for i in range(0,limit):
    
    if Lst[i]==Lst[i+1]:

        duplicate_lst.append(Lst[i])

print(duplicate_lst)        