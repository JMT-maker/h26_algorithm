import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# DP 테이블 초기화 (현재 숫자로 초기화)
dp = [0] * n
dp[0] = arr[0]

for i in range(1, n):
    # 이전 연속합을 이을지, 여기서 새로 시작할지 결정
    dp[i] = max(dp[i-1] + arr[i], arr[i])

print(max(dp))