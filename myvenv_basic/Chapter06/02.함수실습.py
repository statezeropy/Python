# 기본형
# 1. 정의하기
def printHello():
    print("Hello")

# 2. 호출하기
printHello()

# 매개변수가 있는 함수
def sum(a,b):
    print(a + b)

sum(1, 3)

# 반환값이 있는 함수
import numbers
import random
def getRandomNumber():
    number = random.randint(1,10)
    return number

print(getRandomNumber())

# 매개변수와 반환값이 있는 함수
def add(a, b):
    result = a + b
    return result

print(add(5,6))