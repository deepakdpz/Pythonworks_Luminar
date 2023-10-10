# f=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\fileinput\\words.txt","r")

# lst=[]

# for line in f:
#     lst.append(line.rstrip("\n"))

# print(lst)   

# longestword=max(lst,key=lambda w:len(w))
# print(longestword)

# words=[line.rstrip("\n") for line in f ]
# longestword=max(words,key=lambda w:len(w))
# print(longestword)

#--------------------------------------------------

f_read=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\fileinput\\data.txt","r")

odd_write=open("odd.txt","w")

even_write=open("even.txt","w")

for i in f_read:
    num=int(i.rstrip("\n"))

    if num%2==0:
        even_write.write(str(num)+"\n")

    else:
        odd_write.write(str(num)+"\n")    