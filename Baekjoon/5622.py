# 5622 - 다이얼

n = input()
list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = []

for i in n:
    for j in list:
        if i in j:
            result.append(list.index(j) + 3)

print(sum(result))