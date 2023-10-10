# lst=[2,1,4,6,3]

# n=0

# print("original list=",lst)

# for i in lst:
#     n=n+1

# # print(n)


# lst.sort()

# # print(lst)

# for p in range(1,n+1):
#     for i in range(0,n):
#         if n==lst[i]:
#             print(lst)

#         else:
#             # lst.append(n) 
#             break   
           
# lst.append(n) 
# lst.sort()          
# print("new list=",lst)

# ---------------------------------------
lst=[3,1,5,6,4]
lst.sort()

if(lst[0]!=1):
    print("1 is missing")

else: 
    for i in range(0,len(lst)):
        current=lst[i]
        next=lst[i+1]
        diff=next-current
        
        if diff!=1:
            print(current+1,"is missing")

            break
   

# print(len(lst))

