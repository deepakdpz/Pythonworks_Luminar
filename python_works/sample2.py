# def is_fibanocci(num):
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

# num = int(input("enter a number"))

# if is_fibanocci(num):
#     print(f"{num} is a fibonacci number.")
# else:
#     print(f"{num} is not a fibonacci number.")

# -------------------------------------------------



# num=int(input("enter a number:"))

# original=num

# digit_count=len(str(num))

# sum=0


# print(digit_count)

# while(num!=0):
#     last_digit=num%10
#     exponent=last_digit**digit_count
#     sum=sum+exponent
#     num//=10

# if(sum==original):
#     print(f"{original} is armstrong number")  

# else:
#     print(f"{original} is  not armstrong number")     

# ----------------------------------------------------


# range=int(input("enter the range:"))

# start=1

# prev=0
# current=1

# print(prev,end=" ")
# print(current,end=" ")

# while(start<=range):
#     sum=prev+current
#     print(sum,end=" ")
#     (prev,current)=(current,sum)

#     start+=1


# -----------------------------------------------------

# number=int(input("enter the number to find factorial:"))

# start=1

# fact=1



# while(start<=number):
#     fact=fact*start

#     start+=1

# print(fact)    

# ------------------------------------------------------


# num=int(input("enter the number to find multiplication table:"))

# start=0
# end=10

# while(start<=end):
#     c=start*num

#     print(f"{start} *  {num} = {c}")

#     start+=1

# --------------------------------------------------------

# num=int(input("enter a number:"))

# original=num

# reverse=0


# while(num!=0):
#     r=num%10
#     reverse=reverse*10+r
#     num//=10

# if(reverse==original):
#     print("paliondrome")

# else:
#     print("not paliondrome")

# ---------------------------------------------------------

# num=int(input("enter a number"))

# prev=0
# current=1

# is_fibo=False

# fibo_num=0

# while(fibo_num<=num):
#     fibo_sum=prev+current
#     if(fibo_num==num):
#         is_fibo=True
#         break
#     prev=current
#     current=fibo_num
#     fibo_num+=1


# print(is_fibo)

# ---------------------------------------------------------


num=int(input("enter the number"))

start=1

while(start<=num):
    print(str(num)*start)
    start+=1