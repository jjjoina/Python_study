# 지역변수와 전역변수

# 지역변수 : 함수 내에서만 사용하는 변수. 함수가 시작되면 생기고 끝나면 사라진다.
# 전역변수 : 프로그램 내 어디서든지 부를 수 있는 변수

gun = 10

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun을 사용하겠다는 의미
    # gun = 20 # 이 코드를 주석처리하지 않는 것과 비교해보자.
    gun = gun - soldiers # line 9를 명시하지 않으면 이 코드는 에러가 난다. 지역변수 gun의 초기값을 설정해주지 않았기 때문
    print("[함수 내] 남은 총 : {0}".format(gun))

# 많이 사용하는 방법
def checkpoint_ret(gun, soldiers): # checkpoint_return # gun을 변수로 받아버린다.
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun # 이 반환값을 함수 밖에서 사용하면 된다. (line 23)

print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))