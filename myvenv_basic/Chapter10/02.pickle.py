# 1. 파이썬 객체를 pickle로 저장하기
import pickle

data = {
    "목표1" : "매일 팔굽혀 펴기 100회",
    "목표2" : "매일 코딩 공부 1시간",
}

file1 = open("./myvenv/Chapter10/data.pickle", "wb")
pickle.dump(data, file1)
file1.close()

# 2. pickle 파일 파이썬으로 가져오기
file2 = open("./myvenv/Chapter10/data.pickle", "rb")
data = pickle.load(file2)
print(data)
file2.close()