import sys

# 1. 입력 받기
N, M = map(int, sys.stdin.readline().split())

# 2. 두 배열 입력 및 합치기
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

# 3. 리스트 결합 및 정렬
result = A + B
result.sort()

# 4. 결과 출력
print(*(result))