text="ap  ple"

v_count=0
c_count=0
# print vowel count and consonant count

for ch in text:
    if ch in ["a","e","i","o","u"]:
        v_count+=1

    elif ch not in [" ",".","/","!"]:
        c_count+=1

print("vowel count:",v_count) 
print("consonanat count:",c_count)           