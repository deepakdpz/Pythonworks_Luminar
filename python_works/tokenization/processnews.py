news_read=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\tokenization\\news.txt","r")

words_read=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\tokenization\\stopwords.txt","r")

stop_words={line.rstrip("\n") for line in words_read}

news_set=set()

for line in news_read:
    words=line.split(" ")
    for w in words:
        news_set.add(w)

print(news_set.difference(stop_words))        
