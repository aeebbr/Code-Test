# 1929 - 소수 구하기
# m과 n 사이의 소수를 출력

m, n = map(int, input().split())

for i in range(m, n + 1):
    if i == 1:                              # 1은 소수가 아님 => 1 제외
        continue
    for j in range(2, int(i ** 0.5) + 1):   # 2부터 i의 제곱근까지 확인
        if i % j == 0:                      # 약수 존재하면(나누어 떨어지면) break
            break
    else:                                   # 약수 존재하지 않는 소수이면 출력
        print(i)