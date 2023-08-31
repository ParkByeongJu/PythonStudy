import random

try:
    num = random.randint(0, 2)
    result = 10 / num
except Exception as e:
    print('예외발생!!!', e)
else:
    print(f'10/{num} = {result}')
finally:
    print('프로그램 종료....')