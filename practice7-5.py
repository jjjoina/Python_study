# 가변 인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # 팁 : print할 때 끝에 end=" "를 하면 프린트를 하고 줄바꿈을 하지 않고 띄어쓰기로 끝낸다.
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "") # 매번 이렇게 빈 값을 넣기는 불편하다.
# 혹은 유재석이 새로운 언어를 더 할 줄 알게 되면 함수 자체를 새로 정의해 주어야 한다.
# 이럴 때 사용하는 것이 가변 인자이다.

def profile(name, age, *language): # *로 시작하여 가변 인자로 만든다.
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")