# 기본값

def profile(name, age, main_lang):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang)) # 이렇게 역슬래시를 사용해서 두 줄을 하나의 문장으로 처리할 수 있다

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업. 즉 이름만 다른 경우
# 이 때 사용하는 것이 바로 기본값

def profile(name, age=17, main_lang="파이썬"):
    # 함수를 호출할 때 따로 age와 main_lang를 입력하지 않으면 각각 17과 "파이썬"을 부여한다.
    print("이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}" \
        .format(name, age, main_lang))

profile("유재석")
profile("김태호")