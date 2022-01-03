# 문자열포맷

# print("a" + "b")
# print("a", "b")

# 방법 1
print("나는 %d살입니다." % 20) # d는 정수를 의미
print("나는 %s을 좋아해요." % "파이썬") # s는 문자열(string)을 의미
print("Apple은 %c로 시작해요." % "A") # c는 한 글자(character)를 의미
# %s는 정수와 한 글자와도 호환이 된다.
print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간")) # 괄호로 묶어서 여러 개도 가능

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# format 뒤에 있는 괄호의 변수들을 순서대로 0, 1로 인식
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color = "빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color = "빨간", age = 20))

# 방법 4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") # f로 문장을 시작
