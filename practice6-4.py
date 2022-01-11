# continue와 break

absent = [2, 5] # 결석
no_book = [7] # 책을 갖고 오지 않음
for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
    if student in absent:
        continue # 이 이하의 명령문을 실행하지 않고 다음 반복으로 진행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}은 교무실로 따라와.".format(student))
        break # 즉시 반복문을 탈출
    print("{0}, 책을 읽어봐.".format(student))