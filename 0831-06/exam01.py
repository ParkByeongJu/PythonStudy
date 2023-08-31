import random

try:
    num = random.randint(0, 3)
    print('추출된 난수 : ', num)
    data = [10, 20]
    print(10/num)
    print(data[2])

except Exception as e:
    print(e)

# except ZeroDivisionError as e:
#     print('ZeroDividionError 예외 발생!!!', e)
# except IndexError as e:
#     print('IndexError 예외 발생!!!', e)