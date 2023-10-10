txt="pycharm is an ide"

txt.casefold()

words=txt.split(" ")

vowels="a","e","i","o","u"


character_count=0

vowel_count=0

consonant_count=0

for w in words:
    for ch in w:
        character_count+=1

        if ch in vowels:

            vowel_count+=1

        if ch not in vowels:

            consonant_count+=1    




print(character_count) 
print(vowel_count)    
print(consonant_count)   
        