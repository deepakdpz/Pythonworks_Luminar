# full pyramid



num=int(input("enter the number of rows:"))

# for row in range(0,num):
    
#     for spc in range(0,num-row):
#         print(end=" ")

#     for j in range(0,row+1):
#         print("*",end=" ")

#     print()    


for row in range(1,num+1):
    for spc in range(num+1-row,1,-1):
        print(end=" ")

    for col in range(row):
        print("*",end=" ")
    
    print()


 # hollow full pyramid