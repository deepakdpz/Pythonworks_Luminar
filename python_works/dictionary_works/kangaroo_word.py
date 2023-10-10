source_word="chicken"
target_word="henn"

wc={}
is_kangaroo=True

for ch in source_word:
    if ch in wc:
        wc[ch]+=1

    else:
        wc[ch]=1

for ch in target_word:
    if (ch in wc) and (wc.get(ch)>0):
        wc[ch]-=1
        is_kangaroo=True
        
        

    else:
        is_kangaroo=False
        break
           



print(is_kangaroo)        