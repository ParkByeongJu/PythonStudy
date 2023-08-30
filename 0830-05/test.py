age = 23
alpha = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7, 'i':8, 'j':9}
answer = ""

for a in str(age):
    for k, v in alpha.items():
        if int(a) == v:
            answer += k

print(answer)



# for k, v in alpha.items():
#     if v == age:
#         answer += v
