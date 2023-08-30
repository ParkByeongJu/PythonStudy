class Parent:
    def __init__(self):
        self.name = '부모'
        print('Parent() 호출...')
    def info(self):
        print('Parent info() 호출....')

class Child(Parent):
    def __init__(self):
        super().__init__()
        print('Child() 호출...')
    def info(self):
        super().info()
        print('Child info() 호출...')

# p = Parent()
p = Child()
p.info()
print(p.name)
