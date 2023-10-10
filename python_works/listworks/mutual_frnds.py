all_users=["mohanlal","unni","fahad","dq","mammotty","nivin"]

nivin_frnds=["mohanlal","unni","fahad"]
fahad_frnds=["mohanlal","mammotty","unni"]

mutual_frnds=[]

for u in all_users:
    if u in nivin_frnds and u in fahad_frnds:
        mutual_frnds.append(u)

print(mutual_frnds)        