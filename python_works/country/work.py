from json import load

path="C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\country\\countries.json"

with open(path,encoding="utf-8") as f:
    
    countries=load(f)

print(len(countries))    

#-----------------------------------------------------------------------------

# countries in asia

# asian_countries=[c.get("name") for c in countries if c.get("region")=="Asia"]

# print(asian_countries)

#------------------------------------------------------------------------------

# countries with population less than 50 lakhs

# less_than_50=[c.get("name") for c in countries if c.get("population")<=5000000 ]

# print(less_than_50)

#------------------------------------------------------------------------------

# populated country

# populated_country=max(countries,key=lambda c:c.get("population"))

# print(populated_country)
# print(populated_country.get("population"))

#----------------------------------------------------------------------

# less populated country

# less_populated=min(countries,key=lambda c:c.get("population"))


# print(less_populated)

#-----------------------------------------------------------------------

# independent countries


# independent=[c.get("name") for c in countries if c.get("independent")==True]

# print(independent)

#-----------------------------------------------------------------------

#currencies name

# for c in countries:
    # for i in c.get("currencies"):
        # print(i)
# print(currency_names)

#------------------------------------------------------

# country name starts  with c

# filters=[c.get("name") for c in countries if c.get("name").casefold().startswith("C") ]

# print(filters)

#------------------------------------------------------

# country names and capitals

# name_capital=[[c.get("name"),c.get("capital")] for c in countries]

# print(name_capital)

#--------------------------------------------------------

# comtry with max number of borders

# c_with_border=[c for c in countries if "borders" in c]

# max_border_c=max(c_with_border,key=lambda c:len(c.get("borders")))

# print(max_border_c.get("name"))

#-------------------------------------------------------------

# country sharing border with india

# india_borders=[c.get("borders") for c in countries if c.get("name")=="India"][0]

# print(india_borders)

# border_name=[c.get("name") for c in countries if c.get("alpha3Code") in india_borders]

# print(border_name)

#----------------------------------------------------------

#get all regions

# all_regions={c.get("region") for c in countries }

# print(all_regions)

#-------------------------------------------------------

# non independent countries

# dependent_countries=[c.get("name") for c in countries if c.get("independent")==False]

# print(dependent_countries)

#------------------------------------------------------------------------------------------

# no contrys in asia atlantic america antartic

# wc={}

# for c in countries:
#     if c.get("region") in wc:
#         wc[c.get("region")]+=1

#     else:
#         wc[c.get("region")]=1

# print(wc)        