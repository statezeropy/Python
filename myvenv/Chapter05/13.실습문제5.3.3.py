korean = ["가나", "다라", "마바","사자"]


for word in korean:
    print(word)
    test = input("입력 >>> ")
    if test != word:
        print("틀렸어")
        break
