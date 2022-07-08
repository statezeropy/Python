
while True:
    print("1.게임 시작\n2.랭킹 보기\n3.게임 종료")
    menu = int(input("메뉴를 입력하세요 >>>"))
    if menu == 1:
        print("게임을 시작합니다.")
    elif menu == 2:
        print("실시간 랭킹")
    elif menu == 3:
        print("게임을 종료합니다.")
        break
    else:
        print("다시 입력해 주세요")
