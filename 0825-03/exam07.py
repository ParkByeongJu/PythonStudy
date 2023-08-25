# 정수 2개를 입력받아 최대공약수 출력

print("정수 2개를 입력해주세요 : ")

num1 = int(input())
num2 = int(input())

while num2:
    num1, num2 = num2, num1 % num2
print(num1)