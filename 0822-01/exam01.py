# 한줄주석

"""
    정수 2개 입력 받아 사칙연산의 결과 출력
"""

print('첫번째 정수를 입력 : ', end='') # print는 기본적으로 \n가 되어 있고 줄바꿈을 하자 않으려면 ,end=''사용
num01 = int(input())
#print(type(num01))
print('두번째 정수를 입력 : ', end='')
num02 = int(input())

print(num01, '+' ,num02, '=', num01 + num02)
print('%d - %d = %d' % (num01, num02, num01 - num02))
print('%d * %d = %d' % (num01, num02, num01 * num02))
print('%d / %d = %f' % (num01, num02, num01 / num02))
print('{0} / {1} = {2}'.format(num01, num02, num01 / num02))
print(f'{num01} / {num02} = {num01 / num02}') #f는 format String 이라고 부름
print(int(num01 / num02))
print(f'{num01} / {num02} = {num01 // num02}')
print(f'{num01} % {num02} = {num01 % num02}')
print(f'{num01} ** {num02} = {num01 ** num02}')
print('2' * 3)