class Person:
    def __init__(self, name, age, addr):
        self.name = name
        self.age = age
        self.__addr = addr

    @property
    def addr(self):
        return self.__addr

    @addr.setter
    def addr(self, addr):
        self.__addr = addr

    def info(self):
        print(f'name : {self.name}, age : {self.age}, addr : {self.__addr}')


p = Person('홍길동', 25, '서울')

p.info()
print(p.name)
print(p.age)
print(p.addr)
p.addr = '부산'
print(p.addr)