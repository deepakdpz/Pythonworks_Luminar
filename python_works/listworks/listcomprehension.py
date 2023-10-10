# lst=[2,3,4,5,6,7,8]

# squares=[n**2 for n in lst ]

# print(squares)

# cubes=[n**3 for n in lst ]

# print(cubes)

# add_two=[n+2 for n in lst ]

# print(add_two)

#---------------------------------------

# num_grt_five=[n for n in lst if n>5]
# print(num_grt_five)

# evens=[n for n in lst if n%2==0]
# print(evens)
 
# odds=[n for n in lst if n%2!=0]
# print(odds) 

#----------------------------------------

# years from 1800 to 2025

years=[y for y in range(1800,2026) ]

century_yrs=[y for y in years if y%100==0]

non_century_yrs=[y for y in years if y%100!=0]

# print(years)
# print(century_yrs)
print(non_century_yrs)