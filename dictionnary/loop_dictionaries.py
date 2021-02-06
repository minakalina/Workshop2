# EX1
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict:  # ถ้า for in เฮยๆได้แค่ตัวkey
    print(key)
# brand
# model
# year

# EX2
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict:
    print(thisdict[key])  # access dictด้วยkeyจะได้ค่าvalue
# Ford
# Mustang
# 1964

dict_value = thisdict[key]
print(thisdict)
# 1 thisdict["brand"]-> Ford
# 1 thisdict["model"]-> Mustang
# 1 thisdict["year"]-> 1964
# EX3
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key in thisdict.keys():  # ค่าเป้นkey
    print(key)


# EX4
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for value in thisdict.values():  # ค่าเป็น value
    print(value)
# Ford
# Mustang
# 1964

# EX5
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
for key, value in thisdict.items():  # .items ได้ทั้งkey,value
    print(key, value)  # ทั้ง2 ทั้งkeyและ value
# brand Ford
# model Mustang
# year 1964
