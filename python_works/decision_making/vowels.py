word=input("enter a word").casefold()

letter=word[0]

if(letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u"):
    print("vowel")

else:
    print("consonant")    