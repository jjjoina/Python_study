# 사전

cabinet = {3:"유재석", 100:"김태호"} # 사전은 중괄호 # 키 + : + 값

# 값을 가져오는 방법 1
print(cabinet[3])
print(cabinet[100])

# 값을 가져오는 방법 2
print(cabinet.get(3))

# print(cabinet[5]) # 없는 키를 출력하려고 하면 오류가 발생.
print(cabinet.get(5)) # 하지만 get으로 하면 None으로 출력하고 진행.
print(cabinet.get(5, "사용 가능")) # 키가 없을 시 "사용 가능" 출력
print("hi")

# in : 키 존재 유무?
print(3 in cabinet)
print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님
print(cabinet)
cabinet["C-20"] = "조세호"
print(cabinet)
# 만약 이미 사용중인 키면, 값이 업데이트 된다.
cabinet["A-3"] = "김종국"
print(cabinet)

# del : 떠난 손님
del cabinet["A-3"]
print(cabinet)

# .keys() : 사용 중인 키들
print(cabinet.keys())

# .values() : 사용 중인 값들
print(cabinet.values())

# .items() : 사용중인 키값 쌍들
print(cabinet.items())

# .clear() : 목욕탕 폐점
cabinet.clear()
print(cabinet)