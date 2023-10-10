# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}

# print(set1.symmetric_difference(set2))


# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# new=dict(zip(keys,values))
# print(new)

#------------------------------------------

# num=5

# # n=1
# for row in range(1,num+1):
#     n=1
    
#     for  spc in range(num-row):
#         print(end=" ")

#     for col in range(1,row+1):
        

#         print(n,end=" ")
#         n+=1

#     print()        

#------------------------------------------

# p=2

# for row in range(1,6):

#     for col in range(1,5):

#         if row%2!=0:
#             print("*",end=" ")

#         if  (row*p)%2==0 and col==1:
#             print("*",end=" ")  

#     print()        

wd="e"
word="teachr"

is_present=False

for w in word:
    if w==wd:
        is_present=True


print(is_present)
    
if is_present==True:

    word.replace(w,"")

    print(word)
























