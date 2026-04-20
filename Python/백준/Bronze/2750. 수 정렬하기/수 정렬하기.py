import sys

# 1. 데이터 개수 입력
n = int(sys.stdin.readline())

# 2. 데이터를 담을 리스트 생성
numbers = [int(sys.stdin.readline()) for _ in range(n)]

# 3. 제자리 정렬 (원본 numbers가 변경됨)
numbers.sort()

# 4. 결과 출력
for num in numbers:
    print(num)

