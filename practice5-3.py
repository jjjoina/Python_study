# 튜플

# 리스트와 다르게 내용의 추가, 변경 등이 불가능하다.
# 하지만 속도가 빠르다.
# 소괄호

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스")

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby)

# 튜플을 활용하여 한번에 지정 가능
(name, age, hobby) = ("김종국", 20, "코딩")
print(age, hobby, name)