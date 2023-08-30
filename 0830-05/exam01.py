def myPrint(*values, end='>>',sep='\t'):
    for value in values:
        print(value, end=end, sep=sep)

def calc(command, *cal):
    s = 0 if command == 'add' else 1
    for value in cal:
        if command == 'add':
                s += value
        elif command == 'mul':
                s *= value
    return s




myPrint(10)
myPrint(10, 'A')
myPrint((10, 20, 30, 40), [100, 200, 300, 400], end='\n')

print(calc('add', 12, 7))
print(calc('add', 12, 6, 9))
# print(calc('add', 12, [6, 9, 10]))
print(calc('mul', 12, 7))
print(calc('mul', 1, 2, 3, 4, 5))