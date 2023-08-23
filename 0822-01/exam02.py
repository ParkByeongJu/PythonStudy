'''
num01 = input('첫번째 정수 입력 : ')
num02 = input('두번째 정수 입력 : ')
print(num01, num02)
'''

num01, num02 = map(int, input('두개의 정수를 입력 : ').split())
print(type(num01), type(num02))
