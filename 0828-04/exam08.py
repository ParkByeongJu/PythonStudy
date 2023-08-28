'''
    input.txt  읽어 다음의 결과를 출력하시오
    1. 총 단어의 개수 세어보기
    2. 단어의 빈도수 (알파벳순으로 출력)
        a   15
        above 1
        ...
    3. 단어가 몇번째 라인에 나왔는지 출력
        a   15  2, 3, 5, 11, 11, 26, 22
'''

# 1번
with open('input.txt', 'r') as file:
    strCnt = 0
    for line in file:
        result = line.split()
        strCnt += len(result)
        # print(result)
print(f'총단어의 개수 : {strCnt}')

# 2번
with open('input.txt', 'r') as file:
    text = file.read()
    strList = text.split()
    strCnt = {}
    for w in strList:
        strCnt[w] = strCnt.get(w, 0) + 1
        keys = sorted(strCnt.keys())
    for w in keys:
        print(f'{w} : {str(strCnt[w])}')
