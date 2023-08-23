'''
    데이터를 입력하세요
    10 5 23 89 11.2 5 16 'hello' 8

    1단계
     // 정수의 합 : (10 + 5 + 23 + 89 + 5 + 16 + 8)

    2단계
     // 소수 출력 5 23 89 5

    3단계
     //['', 5, 23, 89, '', 5, '', '', '']

    소수 구하기
    num = 29
    i = 2
    while i < num and num % i :
        i += 1
    print('소수' if i == num else '비소수')
'''

data = input('데이터를 입력하세요').split()

for numStr in data :
   if numStr.isdigit() :
       num = int(numStr)
       print(num)
