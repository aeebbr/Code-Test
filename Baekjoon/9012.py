'''
9012 - 괄호

괄호가 짝이 맞으면 YES, 맞지 않으면 NO
(()())((())) => YES
())(() => NO
'''

t = int(input())

for i in range(t):
    bracket = input()
    count = 0
    for j in bracket:
        '''
        ( 가 나오면 +1, ) 가 나오면 -1
        count에 숫자 1을 넣고 빼는 것을 반복
        괄호의 짝이 맞으면 최종 count 값은 0
        '''
        if j == '(':
            count += 1
        elif j == ')':
            count -= 1
        if count < 0:   # )(()    => count가 0인 상태에서 ) 가 먼저 나와 버리면 -1이 됨
            print('NO')
            break
    if count == 0:
        print('YES')
    elif count > 0:
        print('NO')