# def std_weight(height, gender):
#     if gender == "male":
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, height / 100 * height / 100 * 22))
#     else:
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다.".format(height, height * height * 21))

# std_weight(175, "male")

# 답안
def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21

height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2) # 소수점 둘째자리까지 표시 (소수점 셋째자리에서 반올림)
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))