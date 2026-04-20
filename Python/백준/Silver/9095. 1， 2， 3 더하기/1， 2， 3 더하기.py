import sys
input = sys.stdin.readline

def solve(n): # [Comparison] solve 함수는 n이 1, 2, 3인 경우의 결과를 직접 반환하고, 그 외의 경우에는 재귀적으로 solve 함수를 호출하여 결과를 계산합니다.
    if n == 1: return 1 
    if n == 2: return 2
    if n == 3: return 4
    return solve(n-1) + solve(n-2) + solve(n-3)# [Comparison] n이 1, 2, 3인 경우의 결과를 직접 반환하고, 
                                                # 그 외의 경우에는 재귀적으로 solve 함수를 호출하여 결과를 계산
t = int(input())
for _ in range(t):  
    n = int(input())
    print(solve(n))
