import sys

# n: 동전 종류 수, k: 목표 금액
n, k = map(int, sys.stdin.readline().split())

# 동전 가치 리스트 받기
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

# 큰 동전부터 확인하기 위해 뒤집기 (내림차순)
coins.reverse()

count = 0
for coin in coins:
    if k == 0:
        break
    
    # 해당 동전으로 만들 수 있는 최대 개수 더하기
    count += k // coin
    # 남은 금액 업데이트 (나머지 연산)
    k %= coin

print(count)