# for 변수 in 시퀀스 자료:
#   명령문

# range(10) 0~9까지 숫자를 포함하는 range 객체를 생성한다

# 시퀀스 자료형
# : 순서가 있는 자료형
# 1. 리스트
# 2. 문자열
# 3. range 객체
# 4. 튜플
# 5. 딕셔너리

# for 문
# - 리스트 사용
champions = ["티모", "이즈리얼", "리신"]

for champion in champions:
    print("선택한 챔피언은", champion)

# - 문자열 사용
fightin_message = "자신감을 가지자! 나에게 한계란 없다!"
for word in fightin_message:
    print(word)

# - range 객체 사용
# range(10) -> 0~9까지 숫자를 포함하는 range 객체나온다. 
# range(시작, 끝+1, 단계)
for i in range(1, 20, 2):
    print(i)