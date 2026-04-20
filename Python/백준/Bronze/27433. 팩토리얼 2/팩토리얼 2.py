# factorial N recursive로 계산
def fact_r(N):
    # base condition: 재귀가 멈추는 지점
    if N <= 1: 
        return 1
        
    # recursive step: N과 (N-1)!을 곱함
    return N * fact_r(N - 1)

# 사용자로부터 입력 받기
N = int(input())
print(fact_r(N))