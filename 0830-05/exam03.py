def print_book_info(**args):
    for key, value in args.items():
        print(f'{key} : {value}')
    print('=' * 20)

print_book_info(title='홍길동전', writer='허균', price=15000)
print_book_info(title='홍길동전', writer='허균')
print_book_info(title='홍길동전')
print_book_info(title='홍길동전', price=15000)
book = {'title':'홍길동전', 'writer':'허균', 'price':15000}
print_book_info(**book)