import sys

# 입력받기
n = int(sys.stdin.readline())

result = 0

# 1부터 n까지 모든 숫자를 확인 (브루트포스)
for i in range(1, n + 1):
    # 각 자리수의 합 계산 (예: i=245라면 2+4+5)
    digit_sum = sum(map(int, str(i)))
    
    # 분해합 = 숫자 본체 + 각 자리수의 합
    decompose_sum = i + digit_sum
    
    # 분해합이 입력값 n과 같다면 i는 n의 생성자!
    if decompose_sum == n:
        result = i
        break  # 가장 작은 생성자를 찾는 것이므로 처음 발견하면 바로 종료

print(result)