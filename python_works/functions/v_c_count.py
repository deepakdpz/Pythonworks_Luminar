def count(word):

    v_count=0
    c_count=0

    for ch in word:
        if ch in ["a","e","i","o","u"]:
            v_count+=1

        else:
            c_count+=1  

    print("vowel count:",v_count)
    print("consonanat count",c_count)        


word=input("enter a word:").casefold()

count(word)

