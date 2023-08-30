class TV:
    def __init__(self):
        # print('초기화 진행')
        self.power = False
        self.channel = 10

    def info(self):
        print(f'채널정보 : {self.channel}')
        if 'volume' in self.__dict__:
            print(f'음량 : {self.volume}')

tv = TV()
print(tv.power)
tv.info()
tv.volume = 20
print(tv.volume)
tv.info()

class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f'자동차명 : {self.name}\t가격 : {self.price}')

c = Car('그랜저', 4000)
c2 = Car('모닝', 2100)
c.info()
c2.info()