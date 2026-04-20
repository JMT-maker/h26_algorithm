# BOJ 10870 : 피보나치 수 5
# 피보나치수를 recursive로 구하기 

def fibo(n):
    # Base Condition: 0일 때는 0, 1일 때는 1을 반환
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # Recursive Step: 앞의 두 수를 더함
    return fibo(n - 1) + fibo(n - 2)

# 입력 받기
n = int(input())
print(fibo(n))