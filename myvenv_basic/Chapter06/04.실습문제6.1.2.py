def printSumAvg(x,y,z):
    """
    세게의 숫자를 받아 합계와 평균을 출력하는 함수
    """
    sum = x + y + z
    avg = sum / 3
    print("합계 : ", sum, "\n평균", avg)
    print(f"합계 : {sum} 평균 {avg}")

printSumAvg(10, 20, 30)