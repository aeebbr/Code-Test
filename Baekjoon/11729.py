# 11729 - 하노이 탑 이동 순서

import sys

def hanoi(n, start, end, mid):
    if n == 1:
        print(start, end)               # n이 1일 경우, 1에서 3으로 바로 옮김
    else:
        hanoi(n-1, start, mid, end)     # n-1개를 start -> mid -> end 순서대로 옮기도록 함수 호출
        print(start, end)               # 가장 큰 원판을 end로 옮김
        hanoi(n-1, mid, end, start)     # 이동된 n-1개의 원판을 mid -> start -> end 순서대로 옮기도록 함수 호출

n = int(sys.stdin.readline())   # n 입력
print((2**n) - 1)               # 옮겨진 횟수
hanoi(n, 1, 3, 2)               # 하노이 이동 출력