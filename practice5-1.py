# 리스트 [] : 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명이 있다고 해보자.
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# .append()
# 하하씨가 다음 정류장에서 다음 칸에 탐
subway.append("하하")
print(subway)

# .insert()
# 정형돈씨를 유재석씨와 조세호씨 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# .pop()
# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# .cound()
# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# .sort() : 정렬
num_list  = [5,2,4,3,1]
num_list.sort()
print(num_list)

# .reverse() : 순서 뒤집기
num_list.reverse()
print(num_list)

# 리스트는 자료형에 구애받지 않는다.
mix_list = ["조세호", 20, True]
print(mix_list)

# .extend() : 리스트 합치기
num_list.extend(mix_list)
print(num_list)

# .clear() : 모두 지우기
mix_list.clear() # 빈 리스트
print(mix_list)