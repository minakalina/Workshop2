# 1 จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "Python is one of the fastest-growing programming languages"
sentence = "Python is one of the fastest-growing programming languages"
print(len(sentence))

# 2 จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "Python is one of the fastest-growing programming languages"
print(sentence[0])

# 3 จงเขียนคำสั่งเพื่อแสดง "fastest" ของข้อความ "Python is one of the fastest-growing programming languages"

print(sentence[21:28])


# 4 จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ไม่มี space
print(sentence.replace(" ", ""))

# 5 จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมใหญ่ทั้งหมด
print(sentence.upper())

# 6 จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ให้เป็นตัวพิมเล็กทั้งหมด
print(sentence.lower())

# 7 จงเขียนคำสั่งเพื่อแสดข้อความ "Python is one of the fastest-growing programming languages" ที่ถูกแทนที่อักษร r ด้วย x ทั้งหมด
print(sentence.replace("r", "x"))

# 8 จงเติมคำในช่องว่าเพื่อแสดงอายุ
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
