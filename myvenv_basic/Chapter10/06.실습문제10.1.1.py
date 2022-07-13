import csv
import pickle
from turtle import pu


data = [
    ["종목", "매입가", "수량", "목표가"],
    ["삼성전자", 85000, 10, 90000],
    ["NAVER", 380000, 5, 400000],
    ["NC", 860000, 1, 1000000],
]

file = open("./myvenv/Chapter10/mystock.csv", "w", newline="", encoding="utf-8-sig")
writer = csv.writer(file)

for d in data:
    writer.writerow(d)
file.close()

# 파일 읽기

def show_profit(data):
    name = data[0] # 종복
    purchase_price = int(data[1]) # 매입가
    amount = int(data[2]) # 수량
    target_price = int(data[3]) # 목표가

    profit = (target_price - purchase_price) * amount # 수익금
    profit_ratio = (target_price / purchase_price - 1) * 100 # 수익률

    print(f"{name} {profit} {profit_ratio:.2f}%") # :.2f 소수점 2자리

file = open("./myvenv/Chapter10/mystock.csv", "r", newline="", encoding="utf-8-sig")

reader = list(csv.reader(file))
for data in reader[1:]:
    show_profit(data) # 함수 실행

    
file.close()

