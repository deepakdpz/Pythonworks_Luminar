from re import *

f=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\regularexpression\\data.txt")

phone_number=[]
mail_id=[]

phone_rule="\d{10}"
mail_rule="[\w]+@gmail.com"

for lines in f:
    words=lines.rstrip("\n").split()

    for w in words:
        matcher=fullmatch(phone_rule,w)
        
        if matcher!=None:
            phone_number.append(w)

        matcher=fullmatch(mail_rule,w)

        if matcher!=None:
            mail_id.append(w)

print(phone_number)
print(mail_id)            
