# 집합 (set)

# 중복 안 됨, 순서 없음
# 중괄호

my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 이렇게 리스트로 먼저 만들고 set으로 감싸주는 식으로 생성할 수도 있다.

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 줄 알지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# add : 값 추가
python.add("김태호")
print(python)

# remove : 값 제거
java.remove("김태호")
print(java)