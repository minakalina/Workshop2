# EX1
a = 33
b = 200

if b > a:
    print("b is grater than a")
# b is grater than a

# EX2
a = 33
b = 33
if b > a:
    print("b is grater than a")
elif a == b:
    print("a and b are equal")
# a and b are equal

# EX3
a = 200
b = 33
if b > a:
    print("b is grater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is grater than b")
# a is grater than b

# EX4
a = 200
b = 33

max = a if a > b else b
print(max)
# ถ้าเข้าเงื่อนไข ปริ้นค่าที่อยู่ในmax 200


# EX5
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
# Both conditions are True ****ต้องถูกทั้งหมด


# EX6
a = 200
b = 33
c = 500

if a > b or a > c:
    print("At least one of the conditions is True")
# At least one of the conditions is True **ถูกอันนึง


# EX7
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20")
# Above ten,
# and also above 20!

# เข้า2เงื่อนไขได้
