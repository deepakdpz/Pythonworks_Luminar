word=input("enter a word:").casefold()


for ch in word:
    if ch in ["a","e","i","o","u"]:
        
        print(ch,"is a vowel")

    else:

        print(ch,"is not a vowel")    