text="ABBACD"

wc={}
dup_lst=[]

for ch in text:
    if ch in wc:
        dup_lst.append(ch)

    else:
        wc[ch]=1   


print(dup_lst[1])         