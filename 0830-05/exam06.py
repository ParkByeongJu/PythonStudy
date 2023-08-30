class Car:

    addr = '서울'

    __slot__ = ['name', 'price', 'company']

    def __init__(self, **kargs):
        if 'name' in kargs:
            self.name = kargs['name']
        if 'price' in kargs:
            self.price = kargs.get('price')
        if 'company'in kargs:
            self.company = kargs.get('company')
            Car.addr = '부산'
    def info(self):
        if 'company' in self.__dict__:
            print(f'자동차명 : {self.name} 가격 : {self.price} 회사 : {self.company}')
        else:
            print(f'자동차명 : {self.name}  가격: {self.price}')



c = Car(name='그랜저', price=4000, company='현대')
c2 = Car(name='모닝', price=2100)
c.info()
c2.info()
print(c.addr)
print(c2.addr)