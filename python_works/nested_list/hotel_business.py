foods=[ {"id":1,"name":"ghee-roast","price":70,"category":"veg"},
        {"id":2,"name":"chicken-roast","price":170,"category":"non-veg"},
        {"id":3,"name":"cb","price":170,"category":"non-veg"},
        {"id":4,"name":"bb","price":190,"category":"non-veg"},
        {"id":5,"name":"fried-rice","price":140,"category":"veg"},
        {"id":6,"name":"chicken-friedrice","price":170,"category":"non-veg"},
        {"id":7,"name":"nan","price":70,"category":"veg"},
        {"id":8,"name":"alfham","price":370,"category":"non-veg"}
        
]

# total number of items

# print("total number of items=",len(foods))

#-----------------------------------------------

# veg category foods

# for f in foods:
#     if f.get("category")=="veg":
#         print(f.get("name"))

#----------------------------------------------

# food under 100rs

# low=[f.get("name") for f in foods if f.get("price")<100]
# print(low)

#------------------------------------------------------

#costly item

# costly=max(foods,key=lambda f:f.get("price"))
# print(costly)

#-----------------------------------------------------

#costly non veg food

non_veg=[f for f in foods if f.get("category")=="non-veg" ]

costly_non_veg=max(non_veg,key=lambda f:f.get("price"))

print(costly_non_veg)

#-------------------------------------------------------

# print all categories

# categories={f.get("category") for f in foods }

# print(categories)