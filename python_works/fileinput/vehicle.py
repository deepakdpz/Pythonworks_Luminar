f=open("C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\fileinput\\number.txt")

numbers=[n.rstrip("\n") for n in f ]

kerala_numbers=[n for n in numbers if n.startswith("kl")]

print(kerala_numbers)