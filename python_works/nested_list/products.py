items=[
    {"id":1,"name":"sugar","price":40,"avl_qty":10},
    {"id":2,"name":"milk","price":28,"avl_qty":40},
    {"id":3,"name":"teapowder","price":230,"avl_qty":100},
    {"id":4,"name":"tomatto","price":120,"avl_qty":5},
    {"id":5,"name":"potatto","price":45,"avl_qty":70},
    {"id":6,"name":"carrot","price":80,"avl_qty":0},
    {"id":7,"name":"oreo","price":45,"avl_qty":0},
    {"id":8,"name":"hideandseek","price":50,"avl_qty":50},
    
]

# print total number of products

# print(len(items),"products")

#-----------------------------------

# print all products name

# for i in items:
    # print(i.get("name"))

#------------------------------------

# print all in stock product names  

# for i in items:
    # if i.get("avl_qty")>0:
        # print(i.get("name"))  

#------------------------------------

# print product names available under rs50

# for i in items:
    # if i.get("price")<50:
        # print(i.get("name"))

#----------------------------------------

# print product names available in range of 20 to 50


# for i in items:
#     if i.get("price") in range(20,51):
#         print(i.get("name"))


#-------------------------------------------

# all_product_nms=[i.get("name") for i in items]
# print(all_product_nms)

#--------------------------------------------

# in_stock_prdcts=[i.get("name") for i in items if i.get("avl_qty")>0 ]
# print(in_stock_prdcts)

#---------------------------------------------

# price_filter=[i.get("name") for i in items if i.get("price")<=50 ]
# print(price_filter)

#----------------------------------------------------

# range_filter=[i.get("name") for i in items if i.get("price") in range(20,51) ]
# print(range_filter)

#-------------------------------------------------

# costly product

# costly_product=max(items,key=lambda i:i.get("price"))
# print(costly_product)

#---------------------------------------------

# sort based on qnty

product_sort=sorted(items,reverse=True,key=lambda i:i.get("avl_qty"))
print(product_sort)