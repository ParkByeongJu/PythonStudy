def get_number():
    try:
        num = int(input('짝수를 입력하세요'))
        if num % 2:
            raise Exception(f'입력하신 정수는 {num}은 짝수가 아닙니다')
    except Exception as e:
        print('get_number() 예외발생')
        raise
    return num

try:
    num = get_number()
    print(num)
except Exception as e:
    print(e)