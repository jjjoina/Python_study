# 표준 입출력

print("Python", "Java", sep=",", end="?")
# sep(seperate)를 통해 구분 기호 설정 가능
# end를 통해 문장의 끝을 설정. 그리고 다음 print문을 줄바꿈 하지 않음
print("무엇이 더 재밌을까요?")

import sys
print("Python", "Java", file=sys.stdout) # stdout : 표준출력으로 문장 처리
print("Python", "Java", file=sys.stderr) # stderr : 표준에러로 문장 처리

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items(): # 딕셔너리를 쓸 때에는 .items()를 이용하여 키와 값을 가져온다.
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")
    # ljust(8) : 8칸의 공간을 확보하여 왼쪽으로 정렬
    # rjust(4) : 4칸의 공간을 확보하여 오른쪽으로 정렬

# 은행 대기순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
    # zfill(3) : 3칸의 공간을 확보하여 값을 넣되, 값이 없는 공간에는 0을 넣는다

answer = input("아무 값이나 입력하세요 : ")
# 사용자가 입력한 값이 answer에 들어간다
print(type(answer)) # input을 통해 값을 받으면 문자열의 형태로 저장이 된다.
print("입력하신 값은 " + answer + "입니다.")