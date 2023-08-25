'''
    a = list()      # []        [10, 20, 30]
        tuple()     # ()        (10, 20, 30)
        str()       # ""        "Hello"
        dict()      # {}        {key : value, key : value, key : value}
'''

data = {'hong' : 1111, 'kang' : 2222, 'han' : 3333, 'park' : 4444, 'kang' : 5555, 100: '123'}
print(data, type(data))

stuInfo = {'name':'hong', 'age':28, 'score':[100,100,70]}
print(stuInfo)

data = {}
data = dict()
data = dict(name='hong', age=28, addr='seoul')
data = dict([('name', 'hong'), ('age', 28), ('addr', "seoul"),(100, 'max')])
data = dict(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))
print(data, type(data))
print(zip(['name', 'age', 'addr'], ['hong', 28, 'seoul']))