from json import load

path="C:\\Users\\deepa\\OneDrive\\Desktop\\python_works\\read_from_jason\\data.json"

with open(path) as f:
    records=load(f)

# print(records)  

#-----------------------------------------------  

# fw_names=[f.get("name") for f in records]

# print(fw_names)

#------------------------------------------

#top rated framework

# top_rated=max(records,key=lambda f:f.get("rating"))

# print(top_rated)

#--------------------------------------------------

#front end frameworks name

# frnt_names=[f.get("name") for f in records if f.get("side")=="frontend"]

# print(frnt_names)

#python framework names

py_frm_nmes=[f.get("name") for f in records if f.get("launguage")=="python"]

print(py_frm_nmes)