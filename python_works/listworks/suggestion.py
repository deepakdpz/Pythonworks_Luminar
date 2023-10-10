all_users=["mohanlal","fahad","unny","mammotty","nivin"]

nivin_friends=["mohanlal","unny","fahad"]

suggestion_lst=[]

# suggestion for nivin

for u in all_users:
    if u not in nivin_friends:
        suggestion_lst.append(u)

suggestion_lst.pop(suggestion_lst.index("nivin"))   

print(suggestion_lst)


