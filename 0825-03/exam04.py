members = {'홍길동':'1111-2222', '박길동':'3333-4444', '윤길동': '5555-6666'}
print(members.keys())
print(members.values())
print(members.items())

print(f'홍길동 존재여부 : {"홍길동" in members}')
print(f'고길동 존재여부 : {"고길동" in members}')
print(f'고길동 존재여부 : {"3333-4444" in members}')

for data in members:
    #print(data, end=' ')
    print(f'{data} : {members.get(data)}')
print()

for data in members.keys():
    print(data, end=' ')
print()

for data in members.values():
    print(data, end=' ')
print()

nums = [2, 3, 4]
a, b, c = nums # a = nums[0], b = nums[1]
print(f'a:{a}, b:{b}, c:{c}')
print()

for key, values in members.items():
    print(f'{key} : {values}')

keys = ['name', 'age', 'adr']
mem = dict.fromkeys(keys, "")
print(mem)