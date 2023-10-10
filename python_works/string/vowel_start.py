text="Sunil Gavaskar had a no-holds-barred remark on overseas commentators"
word=text.casefold()
words=word.split(" ")

# vowels=["a","e","i","o","u"]

# print(words)


# for w in words:
        
#         if w[0] in vowels:
#                 print(w) 



vowels="a","e","i","o","u"

for w in words:
        if w.startswith(vowels):
                print(w)                