# num=int(input("enter the number to be checked:"))

# range=int(input("enter the range to check:"))

# start=1

# prev=0

# current=1

# if num==0 or num==1:
#     print("the  number is present in the series")

# else:
#     while(start<=range):
#         sum=prev+current
#         prev=current
#         current=sum

        
#         if(sum==num):
#             print("the  number is present in the series")

#         else:
#             print("the number is not present in the series")   


#     start+=1         

# def is_fibonacci(number):
#     if number == 0:
#         return True

#     a, b = 0, 1
#     while b <= number:
#         if b == number:
#             return True
#         a, b = b, a + b

#     return False

# # Test the function
# num = int(input("Enter a number: "))
# if is_fibonacci(num):
#     print(f"{num} is present in the Fibonacci series.")
# else:
#     print(f"{num} is not present in the Fibonacci series.")


# def is_fib_number(num):
#     a = 0
#     b = 1
#     while b<num:
#         c = a+b
#         a = b
#         b = c
#     if b==num or a==num:
#         return True
#     if b > num:
#         return False

# num = 12

# if is_fib_number(num):
#     print(f"{num} is a fibonacci number.")
# else:
#     print(f"{num} is not a fibonacci number.")

# --------------------------------------------------------

# n=int(input("enter the number of rows:"))

# for i in range(0,n):
#     for j in range(0,i+1):
#         print("*",end=" ")

#     print()    

# -------------------------------------------------------

# n=int(input("enter the number of rows"))

# for i in range(n+1,0,-1):
#     for j in range(0,i-1):
#         print("*",end=" ")

#     print() 


#--------------------------------------------------------    


# row=int(input("enter the number of rows:"))


# for i in range(1,row+1):
#     for j in range(1,i+1):
#         print(j,end=" ")

#     print()  


#----------------------------------------------------------


# row=5
# k=5

# for i in range(0,row+1):
#     for j in range(k-i,0,-1):
#         print(j,end=" ")

#     print()    


# ---------------------------------------------------------

values=range(-10,0)

for i in values:
    print(i)




        

