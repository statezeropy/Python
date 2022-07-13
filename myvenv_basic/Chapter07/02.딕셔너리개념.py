# 딕셔너리
# : 사전형태의 자료형

stock_a = {"삼성전자" : 82000, "LG전자" : 15000}

stock_b = {
    "삼성전자" : [81000, 81500, 82000, 81500, 8200],
    "LG전자" : (15000, 149000, 148000, 151000, 152000)
}

stock_c = {
    "삼성전자" : {
        "현재가" : 82000,
        "보유수량" : 5,
        "매수단자" : 81000
    }
}

#print(stock_a)
#print(stock_b)
#print(stock_c)

# 딕셔너리 접근하기
print(stock_a["삼성전자"])
print(stock_c["삼성전자"]["보유수량"])

# 딕셔너리 할당하기
stock_a["삼성전자"] = 85000

# 삭제
del stock_a["LG전자"]
print(stock_a)

# 함수
stock_d = {
    "삼성전자" : 82000,
    "SK하이닉스" : 123000,
    "NAVER" : 370000,
    "카카오" : 133000
}

for item in stock_d.items():
    print(item)

for key in stock_d.keys():
    print(key)

for value in stock_d.values():
    print(value)
