# 실습문제 8.1.1


from tkinter import W


class Item:
    def __init__(self, name, price, weight, isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable
    def sale(self):
        print(f"[{self.name}] 판매")
    def discard(self):
        if self.isdropable:
            print(f"[{self.name}] 버리기 성공")
        else:
            print(f"[{self.name}] 버리기 실패")

class Wearableitem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def wear(self):
        print(f"[{self.name}] 착용하기")
    
class UseableItem(Item):
    def __init__(self, name, price, weight, isdropable, effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"[{self.name}] 사용하기")
    
# 인스턴스 생성
shirt = Wearableitem("셔츠", 10000, 1.5, True, "블링블링")
shirt.wear()
shirt.sale()
shirt.discard()

potion = UseableItem("물약", 1002302, 0.1, False, "투명")
potion.discard()
potion.sale()
potion.use()
