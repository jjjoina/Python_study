# for

# print("대기버호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")
# 이렇게 하나하나 다 적으면 불편하다. 이럴 때 사용하는 게 for

for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))
# 리스트 안에 있는 값들이 하나씩 waiting_no에 들어간다.

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))
# range(값) : 0부터 값 미만의 정수를 하나씩 부여

for waiting_no in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_no))
# range(값1, 값2) : 갑1부터 갑2 미만의 정수를 하나씩 부여

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))