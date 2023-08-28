def getTotal(a, b, c, d):
    return a+b+c+d

def getSum(*nums):
    # print(nums, type(nums))
    s = 0
    for n in nums:
        s += n
    return s

data = [10, 20, 30, 40]

print(data)
print(*data)
print(*[10, 20, 30, 40])    # print(10, 20, 30, 40)



print(f'총합 : {getTotal(1, 2 ,3 ,4)}')
print(f'총합 : {getTotal(10, 20 ,30 ,40)}')
print(f'총합 : {getTotal(*data)}')
print(f'총합 : {getTotal(*[10, 20, 30, 40])}')

print(getSum(10, 20, 30, 40))
print(getSum(10, 20, 30, 40, 50, 60))
print(getSum(10, 20))
