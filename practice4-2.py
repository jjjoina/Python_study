# 슬라이싱

inhwa = "980415-1234567"

print("성별 : " + inhwa[7]) # 컴퓨터에서 index는 0부터 시작함!
print("연 : " + inhwa[0:2]) # 0부터 2 직전까지
print("월 : " + inhwa[2:4])
print("일 : " + inhwa[4:6])

print("생년월일 : " + inhwa[:6]) # 처음부터 6 직전까지
print("뒤 7자리 : " + inhwa[7:]) # 7부터 끝까지
print("뒤 7자리 (뒤부터) : " + inhwa[-7:]) # 뒤에서 7번째부터 끝까지