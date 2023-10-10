text=input("enter a word:").casefold()

# print vowels

for ch in text:
    # print(ch,end=" ")
    if ch in ["a","e","i","o","u"]:
    # if (ch=="a" or ch=="e" or ch=="i" or ch=="o"or ch=="u"):
        print(ch,end=" ")
        
