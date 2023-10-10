num=int(input("enter a number:"))

prev=0
current=1
fib_num=0

is_fibo=False

while(fib_num<=num):
    fibo_num=prev+current
    if(fibo_num==num):
        is_fibo=True
        break
    prev=current
    current=fibo_num
    fib_num+=1
print(is_fibo)
