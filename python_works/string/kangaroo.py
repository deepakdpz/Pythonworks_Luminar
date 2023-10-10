word1=input("enter a word:")

word2=input("enter another word:")

srt1=sorted(word1)

srt2=sorted(word2)

flag=0

if(set(srt2).issubset(set(srt1))):
    flag=1
if(flag):
     print("kangaroo")

else:
    print("not kangaroo")    


  
