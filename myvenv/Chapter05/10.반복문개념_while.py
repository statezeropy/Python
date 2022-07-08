# 초기식
# while 조건식:
# 반복할 명령
# 증감식

i = 0
while i < 10:
    print(i)
    i += 1

# 무한 루프 + if문
i = 0
while True:
    i+=1
    if i > 4:
        print(i,"번째 나는 탈출하겠어")
        break

while True:
    x = input("종료하려면 exit를 입력하세요 >>> ")
    if x == "exit":
        break