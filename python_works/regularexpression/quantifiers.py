from re import *

# text="aabbcaaabcaghaaaaa"

# pattern="a+"  # one or more occurance of a
# pattern="a*"    #zero or more occurance of a

# pattern="a{1,2}"

# matcher=finditer(pattern,text)

# for m in matcher:
    
    # print(m.group(),m.start())

#-------------------------------------------------------------

phone=input("enter a number")

rule="\d{10}"

matcher=fullmatch(rule,phone)

if matcher!=None:
    print("valid")

else:
    print("invalid")    
