국어 = int(input("국어 >>> "))
수학 = int(input("수학 >>> "))
영어 = int(input("영어 >>> "))

평균 = (국어 + 수학 + 영어)/3

#if 국어 > 100 or 수학 > 100 or 영어 > 100 or 국어 < 0 or 수학 < 0 or 영어 < 0:
if 0 <= 국어 <= 100 and 0 <= 수학 <= 100 and 0 <= 영어 <= 100:
    if 평균 >= 80:
        print("불합격")
    else:
        print("합격")
else:
    print("잘못 입력하였습니다.")
