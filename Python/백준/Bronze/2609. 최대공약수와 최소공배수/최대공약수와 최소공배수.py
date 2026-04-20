# 1. 두 자연수 입력받기
a, b = map(int, input().split())

# 2. 최대공약수(GCD)를 구하는 함수 정의 (유클리드 호제법)
def get_gcd(n, m):
    # m이 0이 될 때까지 반복
    while m > 0:
        # n을 m으로 나눈 나머지를 사용하여 n, m을 갱신
        n, m = m, n % m
    return n

# 3. 최대공약수 계산
gcd_result = get_gcd(a, b)

# 4. 최소공배수(LCM) 계산
# 공식: (두 수의 곱) // 최대공약수
lcm_result = (a * b) // gcd_result

# 5. 결과 출력
print(gcd_result)
print(lcm_result)