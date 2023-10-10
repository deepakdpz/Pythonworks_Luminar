from re import *

text="abcd123STr@we"

# pattern="\d" #[0-9] \d
# pattern="\D"   #[^0-9] \D
# pattern="\w"   #[a-zA-Z0-9]
pattern="\W"   #specialcharacters


matcher=finditer(pattern,text)

for m in matcher:
    print(m.start(),m.group())