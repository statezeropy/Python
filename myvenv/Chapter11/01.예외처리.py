# 원화를 입력, 환율 입력 -> 달러값

from tkinter import E


won = input("원화 >>> ")
dollar = input("환율 >>> ")
try: # 예외가 발생 할 수 있는 코드
    print(int(won) / int(dollar))
except ValueError :# 에외가 발생 했을 시 실행할 코드
    print("예외가 발생했습니다.", ValueError)
except ZeroDivisionError as e : # 에러 코드 as e 로 에러 보여주기
    print("나누기 0은 불가능 합니다.", e)
except: # 알수 없는 에러
    print("알 수 없는 에러")
else:
    print("예외가 발생하지 않았을 경우 실행")
finally: # 예시) 파일 닫기
    print("예외 발생 유무 상관 없이 실행되는 코드")