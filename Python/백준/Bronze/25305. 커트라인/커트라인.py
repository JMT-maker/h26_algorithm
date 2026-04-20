import sys

n, k = map(int, sys.stdin.readline().split())# n은 학생 수, k는 커트라인 등수
scores = list(map(int, sys.stdin.readline().split())) # 학생들의 점수를 리스트로 입력받음
scores.sort(reverse=True) # 내림차순 정렬
print(scores[k - 1]) # k번째로 큰 점수 출력