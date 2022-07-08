korean = ["가나", "다라", "마바","사자"]

score = 0


for word in korean:
    print(word)
    test = input("입력 >>> ")
    if test != word:
        print("틀렸어")
        #break
        
    else:
        print("정답")
        score += 1
        
print("전체 문제 개수 : ", len(korean))        
print("정답 횟수 : ", score)
print("오답 횟수 : ", len(korean) - score)