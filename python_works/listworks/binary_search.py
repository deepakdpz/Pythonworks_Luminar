# binary search

lst=[10,2,13,15,14]

lst.sort()

is_present=False

element=13



lower=0
upper=len(lst)-1


while lower<=upper:

    middle=(lower+upper)//2


    if element==lst[middle]:
        is_present=True
        break

    elif element<lst[middle]:

        upper=middle-1

    elif element>lst[middle]:

        lower=middle+1



print(is_present)