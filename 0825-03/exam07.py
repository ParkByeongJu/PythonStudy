# 정수 2개를 입력받아 최대공약수 출력

print("정수 2개를 입력해주세요 : ")

num1 = int(input())
num2 = int(input())

while num2:
    num1, num2 = num2, num1 % num2
print(num1)

############################################################

num, num2 = map(int,input('정수 2개 입력하세요 : ').split())
print(num, num2)

divNum = set([i for i in range(1, num+1) if num % i == 0])
divNum2 = set([i for i in range(1, num2+1) if num2 % i == 0])

divisor = [n for n in divNum if n in divNum2]

print(f'{num} 약수들의 집합 : {divNum}')
print(f'{num2} 약수들의 집합 : {divNum2}')

print(divisor)
print(f'최대공약수 : {max(divisor)}')
print(f'최대공약수 : {max(divNum & divNum2)}')