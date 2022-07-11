import pay_module

# 변수 사용
print(pay_module.version)

# 함수 사용
pay_module.printAuthor()

# 클래스 사용
pay_info = pay_module.Pay("A102030", 13000, "2022-07-11") # 폴더에 __pycache__ 생성됨. 캐시 파일
print(pay_info.get_pay_info())

print(pay_module.__name__)