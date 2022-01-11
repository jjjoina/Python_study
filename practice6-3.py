# while

customer = "토르"
person = "Unknown"

while person != customer: # 이 조건을 만족할 때까지 아래를 계속 반복
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
    # 토르가 와야만 반복문을 탈출