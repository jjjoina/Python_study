# 전달값과 반환값

def deposit(balance, money): # 잔액, 입금액
    print("입금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 출력값

balance = 0 # 초기 잔액
balance = deposit(balance, 1000) # balance = 함수의 출력값
print(balance)

# 출금 함수
def withdraw(balance, money):
    if balance >= money: # 잔액이 출금액보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 400)

def withdraw_night(balance, money): # 저녁에 출금, 수수료 붙음
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 두 개의 변수를 tuple 형식으로 반환

balance = 1000
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))