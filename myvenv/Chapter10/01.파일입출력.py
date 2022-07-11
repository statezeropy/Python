# 1. 파일 쓰기
# 경로지정
# 인코딩 해야 한들이 안 깨짐

file = open("./myvenv/Chapter10/data.txt", "w", encoding="utf8")
file.write("1.문자열 덮어쓰기\n")
file.close()

# 2. 파일추가
file = open("./myvenv/Chapter10/data.txt", "a", encoding="utf8")
file.write("2.문자열 이어쓰기")
file.close()

# 3. 파일 읽기
file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")

# 3.1 파일 전체 읽기
data = file.read()
print(data)
file.close()

# 3.2 파일  한 줄 읽기
file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")
while True:
    line = file.readline()
    print(line, end="")
    if line == "":
        break
file.close()