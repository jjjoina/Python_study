# 문자열처리함수

python = "Python is Amazing"
print(python.lower()) # 모든 문자가 소문자로 됨
print(python.upper()) # 모든 문자가 대문자로 됨
print(python[0].isupper()) # 0번쨰 문자가 대문자인가?
print(len(python)) # 문자열의 길이
print(python.replace("Python", "Java"))
# 문자열 python에서 "Python"을 찾아서 "Java"로 대체

index = python.index("n") # 문자열 python에서 "n"의 위치?
print(index)
index = python.index("n", index + 1)
# 두 번째 변수는 스타트 위치, 즉 line 8에서 찾은 "n" 이후의 "n"의 위치?
print(index)

print(python.find("n"))
print(python.find("Java"))
print(python.index("Java"))
# find는 찾고자 하는 문자열이 없으면 -1을 출력하고 코드가 진행되지만 index는 에러가 발생한다.

print()