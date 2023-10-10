number=int(input("enter a number:"))

original=number

sum=0

digit_count=len(str(number))

while(number!=0):
    last_digit=number%10
    exponent=last_digit**digit_count
    sum=sum+exponent
    number//=10

print("armstrong number" if sum==original else "not armstrong")    