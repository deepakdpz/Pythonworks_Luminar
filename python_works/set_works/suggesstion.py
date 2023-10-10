all_users=["sachin","dhoni","kohli","rohit","sanju","padikkal"]

sanju_following=["padikkal","sachin"]

# all_users.pop(all_users.index("sanju"))

# print(all_users)

# st1=set(all_users)

# st2=set(sanju_following)

# suggestion=st1.difference(st2)

suggestion=list(set(all_users).difference(set(sanju_following)))

suggestion.pop(suggestion.index("sanju"))

print(suggestion)