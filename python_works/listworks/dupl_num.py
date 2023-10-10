lst=[2,1,5,3,6,5,1,5]

lst.sort()

dup_list=[]

for i in range(0,len(lst)-1):
    if lst[i]==lst[i+1]:
         if lst[i] not in dup_list:
           dup_list.append(lst[i])
         
print(dup_list)
       