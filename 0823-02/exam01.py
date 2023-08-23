'''
    list 내장함수
    append : 데이터를 추가하기 위한 목적, 맨 마지막에 추가
    insert : 데이터를 추가하기 위한 목적, 특정 위치에 추가
    pop    : 데이터 삭제, 맨 마지막 요소를 삭제
    remove : 데이터 삭제, 특정 데이터를 삭제
    index  : 특정 값의 위치를 검색
    count  : 특정 값의 빈도수
    reverse: 위치 뒤집기 
    sort   : 정렬
    clear  : 리스트 요소 전부 삭제 
'''

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
deldata = data.pop()
print('삭제된 값 : ', deldata)

data = list()
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30)
print(data, id(data))
deldata = data.pop()
print('삭제된 값 : ', deldata)

data = []
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop(0)
print('삭제된 값 : ', delData)

data = [10, 20, 30, 40, 30]
idx = data.index(30)
cnt = data.count(30)
print('위치 : ', idx)
print('개수 : ', cnt)
print('before : ', data)
data.remove(30)
print('after : ', data)

for i in range(len(data)):
    print(data[i], end=' ')
print()

for d in data:
    print(d, end=' ')
print()

# ite = iter(data)
# print(next(ite))

for d in iter(data) :
    print(d, end=' ')
print()

for index, d in enumerate(data):
    print(f'[{index}] : {d}')

print()

for index, d in enumerate(data, start=1):
    print(f'[{index}] : {d}')

print(data[-1])
print(data[-2])

data.reverse()
for d in iter(data) :
    print(d, end=' ')
print()
data.reverse()

for i in range(1, len(data) + 1):
    print(data[-i], end=' ')
print()

# data2 = reversed(data)
# print('data : ', data)
# print('data2 : ', next(data2))

for d in reversed(data) :
    print(d, end=' ')
print()

# data.sort()
# print(data)

print(sorted(data, reverse=True)) # reversed 속성 False(오름차순), =True(내림차순)
print(data)

data = [10, 20, 30]
# for i in range(len(data)):
# #   data.pop(0)

# data.clear()

del data[:]

print(data)

