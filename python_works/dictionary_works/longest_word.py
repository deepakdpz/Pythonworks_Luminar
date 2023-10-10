text="hello good hello goodmorning hai"

words=text.split(" ")


longest_word=max(words,key=lambda w:len(w))

print(longest_word)


# smallest_word=min(words,key=lambda w:len(w))

# print(smallest_word)


# srt_words=sorted(words,key=lambda w:len(w),reverse=True)


# print(srt_words)
