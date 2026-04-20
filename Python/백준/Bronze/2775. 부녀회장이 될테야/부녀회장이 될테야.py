import sys

# 테스트 케이스 개수
t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline()) # 층
    n = int(sys.stdin.readline()) # 호

    # 0층 리스트 초기화 (1호부터 n호까지)
    f0 = [x for x in range(1, n + 1)] # 0층의 i호는 i명

    # k층까지 반복
    for i in range(k):
        # 각 호수마다 아래층의 합을 구함
        for j in range(1, n):
            f0[j] += f0[j-1]
            
    print(f0[-1])