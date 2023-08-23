"""
    quit가 나올때까지 정수를 입력받아 각 정수의 약수를 출력
    10
    6
    36
    87
    23
    40
    quit
    10의 약수 : [1, 2, 5, 10]
    6의 약수 : [1, 2, 3, 6]
    36의 약수 : [1, 2, 3, 4, 6, 9, 12, 18, 36]
    ...
    40의 약수 [1, 2, 4, 5, 8, 10, 20 ,40]
"""

data = []
str = ""

while str != "quit":
    print("정수를 입력하시오(종료하려면 quit 입력) : ")
    str = input()
    data.append(str)

data.pop()
data = list(map(int, data))

for i in data:
    print(f'{i}의 약수 : ', end='')
    for j in range(1, i+1):
        if i % j == 0:
            print(j, end=' ')
    print()
# print(data)
