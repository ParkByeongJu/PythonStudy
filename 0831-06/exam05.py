class NotEvenException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

def get_number():
    try:
        num = int(input('짝수를 입력하세요'))
        if num % 2:
            raise NotEvenException(f'입력하신 정수는 {num}은 짝수가 아닙니다')
    except Exception as e:
        print('get_number() 예외발생')
        raise
    return num

try:
    num = get_number()
    print(num)
except NotEvenException as e:
    print(e)