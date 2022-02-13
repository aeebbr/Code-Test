# 11866 - 요세푸스 문제 0
# n명의 사람 중 k번째 사람 제거 => 모두 제거될 때까지 제거 반복

from collections import deque

n, k = map(int, input().split())        # test case: n = 7, k = 3
queue = deque(list(range(1, n + 1)))

print('<', end="")

for i in range(n - 1):
    queue.rotate(-(k - 1))              # 왼쪽으로 2회 회전
    print(queue.popleft(), end=", ")

    '''
    초기: deque([1, 2, 3, 4, 5, 6, 7])
    
    deque([3, 4, 5, 6, 7, 1, 2])
    deque([6, 7, 1, 2, 4, 5])
    deque([2, 4, 5, 7, 1])
    deque([7, 1, 4, 5])
    deque([5, 1, 4])
    deque([1, 4])
    '''

    # <3, 6, 2, 7, 5, 1,

print(queue.popleft(), end='>')
# <3, 6, 2, 7, 5, 1, 4>