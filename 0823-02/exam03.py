# 1 ~ 10 사이의 정수 10개를 원소로 가지는 리스트 data 선언

# 방법1
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 방법2
# data = list()
# for i in range(10):
#     data.append(i + 1)

# 방법3
# data = [i+1 for i in range(10) if (i+1) % 2]
data = [2*i+1 for i in range(10)]
print(data)

# 구구단 데이터 생성
dan = 4
guguData = [dan * i for dan in range(2, 10)
                        for i in range(1, 10)]
print(guguData)

strData = ['hello', 'good', 'bye', 'welcome', 'apple', 'sorry']
fiveStrData = [s for s in strData if len(s) == 5]
print(fiveStrData)

copyStrData = strData[:]
copyStrData2 = strData.copy()

print('strData : ', strData, id(strData))
print('copyStrData : ', copyStrData, id(copyStrData))
print('copyStrData2 : ', copyStrData2, id(copyStrData2))
