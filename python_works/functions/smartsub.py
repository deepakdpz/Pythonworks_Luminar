def sub(n1,n2):
    if(n1>n2):
        ans=n1-n2
        return ans

    else:
         ans=n2-n1
         return ans
    

print(sub(10,100))    



def sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

print(sub(10,6))
             