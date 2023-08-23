data = [10, 40, 20, 70, 50, 60, 30, 50]

# maximun = data[0]
# minimum = data[0]
#
# for d in data:
#     if minimum > d:
#         minimum = d
#     if maximun < d:
#         maximun = d

sortData = sorted(data)
maximun = sortData[-1]
minimum = sortData[0]

print(f'가장 큰수 : {maximun}, 가장 작은수 : {minimum}')
print(f'가장 큰수 : {max(data)}, 가장 작은수 : {min(data)}')
print(f'총합 : {sum(data)}')