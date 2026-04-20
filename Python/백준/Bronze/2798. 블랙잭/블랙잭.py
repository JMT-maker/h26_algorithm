import sys
from itertools import combinations

# 입력 받기
n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

max_sum = 0

# cards 리스트에서 3개를 뽑는 모든 조합 확인
for combo in combinations(cards, 3):
    current_sum = sum(combo)
    
    # 합이 m을 넘지 않으면서 현재 최댓값보다 크면 갱신
    if current_sum <= m:
        max_sum = max(max_sum, current_sum)

print(max_sum)