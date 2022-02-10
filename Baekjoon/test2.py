'''
        ~
20 + 2 + 0 = 22
21 + 2 + 1 = 24
22 + 2 + 2 = 26
23 + 2 + 3 = 28
24 + 2 + 4 = 30
25 + 2 + 5 = 32
        ~

=> 셀프 넘버: ... ~ 23, 25, 27, 29, 31 ~ ...
'''

allList = list(range(1, 10001)) # 1부터 10000까지
addList = []                    # 생성자
selfNumber = []                 # 셀프 넘버

for i in range(1, 10001):
    result = sum(map(int, str(i)))
    # i = 20, result = 2 + 0
    # i = 21, result = 2 + 1
    addList.append(result + i)
    # 20 + 2 + 0
    # 21 + 2 + 1

selfNumber = list(set(allList) - set(addList))  # allList와 addList의 차집합

for j in sorted(selfNumber):
    print(j)