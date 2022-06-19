# list와 같지만 변경할 수 없는 tuple, ()를 사용
days = ("Mon", "Tue", "Wed", "Thur", "Fri")

print(type(days))

name = "rakhyun"
age = 29
korean = True
fav_food = ["kimchi", "rice"]

# dictionary
rakhyun = {
    "name": "rakhyun",
    "age": 29,
    "korean": True,
    "fav_food": ["kimchi", "rice"]
}

print(rakhyun["name"])
print(rakhyun)
rakhyun["handsome"] = True
print(rakhyun)