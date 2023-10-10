
def max_word(*args):
        
        lengthy=max(args,key=lambda w:len(w))
        print(lengthy)

max_word("good","tea","morning")        

