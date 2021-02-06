# def add_number(number):
#     return number+1

# number = 1
# result = add_number(number)
# print("result",result)

# #result 2


def edit_dict(dict):
    dict["owner"] = "BB"


cup = {"name": "Nantachaporn cup", "age": 21}
edit_dict(cup)

print("profile", cup)

# profile {'name': 'Nantachaporn cup', 'age': 21, 'owner': 'BB'}
# Refตามobjectที่เปลี่ยนไป
# ดูแบบนี้มันดูแค่address valueเปลี่ยนก็ไม่เป็นไรยังไงก็addressตัวเดิม
# มันref เปลี่ยนไปหมด
# ถ้าเวลาทำงานควรระวังเวลาใช้มันเป็นref valueจะเปลี่ยนไป ชีวิตชิบหายแน่

# E.g. BE CAREFUL

# def edit_dict(dict):
#     dict["owner"] = "BB"

# cup = {}
# print("[1]", cup)
# edit_dict(cup)
# print("[2]", cup)

# Output
# [1] {}
# [2] {'owner': 'BB'} <---ไม่เหมือนเดิมละ
