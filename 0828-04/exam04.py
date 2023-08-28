'''
    open(파일명, 모드) # r  /  w
    read()/write()
    close()

    with open() as 파일객체 :
        read()/write()
'''

# file = open('test.txt', 'w')
# file.write('Hello World')
# file.close()

# file = open('test.txt', 'r')
# data = file.read()
# file.close()

with open('test.txt', 'r') as file:
    data = file.read()

print(f'읽어온 데이터 : {data}')