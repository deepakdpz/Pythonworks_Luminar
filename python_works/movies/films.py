from json import load

path="C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\movies\\mdb.json"

with open(path,encoding="utf-8") as f:
    movies=load(f)

print(len(movies))    

#-----------------------------------

# print the movie names

# movie_names=[m.get("title") for m in movies ]

# print(movie_names)

#-----------------------------------------------

# print movie names released in 2005

# movies_2005=[m.get("title") for m in movies if m.get("year")=="2005"]

# print(movies_2005)

#-------------------------------------------------

# print movie titles whose genres is comedy

# comedy_movies=[m.get("title") for m in movies if "Comedy" in m.get("genres")]
# print(comedy_movies)

#-----------------------------------------------------

#lengthy movie title

# lengthy_movie=max(movies,key=lambda m:int(m.get("runtime")))

# print(lengthy_movie)

#------------------------------------------------------

# print all genres

# genres={g for m in movies for g in m.get("genres")}

# print(genres)

#------------------------------------------------------

# comedy movies released in 2015

# comedy_movies2015=[m.get("title") for m in movies if "Comedy" in m.get("genres") and m.get("year")=="2015"]

# print(comedy_movies2015)

#-----------------------------------------------------------

# year that released more movies

# wc={}

# for m in movies:
#     year=m.get("year")

#     if year in wc:
#         wc[year]+=1

#     else:
#         wc[year]=1

# print(max(wc,key=lambda k:wc.get(k)))          