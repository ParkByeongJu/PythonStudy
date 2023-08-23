num = int(input('정수 입력 : '))

if num > 0 :
    if num % 2:
        print(num, ': 홀수')
    else :
        print(num, ': 짝수')
else :
    print("짝/홀 판단은 양수만 가능합니다")

if num < 0 :
    print("짝/홀 판단은 양수만 가능합니다")
elif num % 2 :
    print(f'{num}은 홀수 입니다.')
else :
    print(f'{num}은 짝수 입니다.')

# import random
#
# r = int(random.random() * 10)
#
# if r % 2 == 0:
#     print(f'{r} : 짝수')
# else:
#     print(f'{r} : 홀수')