with open("./myvenv/Chapter10/data.txt", "r", encoding="utf8") as file:
    data = file.read()
    print(data)

# 위의 3줄은 아래의 4줄과 같은 역할
file = open("./myvenv/Chapter10/data.txt", "r", encoding="utf8")
data1 = file.read()
print(data1)
file.close()