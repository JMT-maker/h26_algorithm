# 1. 입력받기
N, K = map(int, input().split())

# 2. 약수를 저장할 빈 리스트 생성
divisors = []

# 3. 1부터 N까지 반복하며 약수 찾기
for i in range(1, N + 1):
    # N을 i로 나누었을 때 나머지가 0이면 약수
    if N % i == 0:
        divisors.append(i)

# 4. K번째 약수 출력하기
if len(divisors) >= K:
    print(divisors[K - 1])
else:
    print(0)