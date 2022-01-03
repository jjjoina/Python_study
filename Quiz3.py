url = "http://naver.com"

pw = url[7:]
index = pw.index(".")
pw = pw[:index]
pw = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"

print(pw)

# 답안
my_str = url.replace("http://", "") # 규칙1
my_str = my_str[:my_str.index(".")] # 규칙2 my_str[0:5] -> 0 ~ 5 직전까지.
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))