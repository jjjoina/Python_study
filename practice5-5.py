# 자료구조의 변경

menu = {"커피", "우유", "주스"} # 집합(set)
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

# 출력문의 괄호 종류 다름!! 소괄호, 중괄호, 대괄호

menu = set(menu)
print(menu, type(menu))