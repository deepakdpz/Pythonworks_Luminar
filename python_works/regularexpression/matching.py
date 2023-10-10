from re import *

# text="abababcdab"

# matcher=finditer("ab",text)

# count=0

# for m in matcher:
#     print(m.start(),m.group())
#     count+=1

# print(count) 

#-------------------------------------------------

# text="abcde5ABCD7kfg"

# pattern="[0-9]" #chck for digits
# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

#-------------------------------------------------
# text="aBadfhjkDDRYI897"

# pattern="[a-zA-Z]" #both lower and upper case

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

#-------------------------------------------------
# text="aBadfhjkDDRY__I897"

# # pattern="[a-zA-Z0-9]" #letters and numbers
# pattern="[^0-9]" #except numbers

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())

#--------------------------------------------------
# how many vowels

# text="abghimuseAIto"

# pattern="[aeiouAEIOU]"   

# count=0

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.start(),m.group())
#     count+=1

# print(count)   

#---------------------------------------------------
# consonants

text="Ahelloth_ere@12"

pattern="[^aeiou_\W\d]"


matcher=finditer(pattern,text.casefold())

for m in matcher:
    
        print(m.group())



    

