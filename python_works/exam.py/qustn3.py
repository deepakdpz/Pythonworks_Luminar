Lst1=[10,11,13,15,] 
Lst2=[9,8,11,13,14] 

Lst1.sort()
Lst2.sort()

common_elements=[]

p1,p2=0,0

while (p1<len(Lst1)) and (p2<len(Lst2)):

    if  Lst1[p1]==Lst2[p2]:

        common_elements.append(Lst1[p1])

        p1+=1
        p2+=1

    elif Lst1[p1]<Lst2[p2]:

        p1+=1

    elif Lst1[p1]>Lst2[p2]:

        p2+=1

print(common_elements)            