# if

# weather = "미세먼지"
weather = input("오늘 날씨는 어때요? ") # input에 대해서는 나중에 배운다.
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요.")
# 조건 중 하나에 들어맞으면 조건문을 탈출한다.

temp = int(input("기온은 어때요? "))
if 30 <= temp :
    print("너무 더워요. 나가지 마세요.")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10: # and 없이 이렇게 표현할 수도 있다. 16번 줄과 비교.
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")