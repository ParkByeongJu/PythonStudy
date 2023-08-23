'''
    *
    **
    ***
    ****
    *****
'''

for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

for i in range(5):
    print('*' * (i+1))

for i in range(9):
    if i < 5:
        print('_' * (i+1))
    else:
        print('_' * (9-i))

for i in range(9):
    # 참문장 if 조건식 else 거짓문장
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)


import random

r = random.randint(20, 50)

result = ""

for i in range(1, r + 1):

    if i % 10 == 0:
        result += "뽀숑" + "\n"
    elif i % 3 == 0 or '3' in str(i):
        result += "짝" + "\n"
    else:
        result += str(i) + "\n"

print(result)
