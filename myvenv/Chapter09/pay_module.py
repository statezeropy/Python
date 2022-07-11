# Paths 설정
# file -> 기본설정 -> 설정 -> 화면 우측상단 '설정 열기(JOSN)'  -> 중간에 아래 내용 추가
# ,
# "python.analysis.extraPaths":["./myvenv/Chapter09"]

# 결제 정보, 관리 모듈
# 변수
version = 2.0

# 함수
def printAuthor():
    print("스타트코딩")

# 클래스
class Pay:
    def __init__(self, id, price, time):
        self.id = id
        self.price = price
        self.time = time
    def get_pay_info(self):
        return f"{self.time} {self.id} {self.price}"

if __name__ == "__main__":
    print("pay module 실행")

print(__name__)