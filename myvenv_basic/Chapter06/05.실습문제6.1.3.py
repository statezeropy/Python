import random

def getRandomNumber():
    number = random.randint(1,45)
    return number

data = []

while True:
    num = getRandomNumber()
    #data.append(getRandomNumber())
    if num in data:
        continue
    #if num not in data:
    #    data.append(getRandomNumber())
    data.append(num)

    if len(data) >= 6:
        data.sort()
        for n in data:
            print(n, end=" ")
        #print(data)
        break
