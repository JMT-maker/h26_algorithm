import sys

n = int(sys.stdin.readline())

members = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    members.append((int(age), name))
# 가입 순서는 Python의 기본 정렬(Stable Sort)이 보장해주므로 '나이'만 기준으로 정렬
members.sort(key=lambda x: x[0])  
# lambda 함수는 각 회원 정보를 (나이, 이름) 튜플로 변환하여 정렬 기준으로 사용함
# sort() 메서드는 리스트를 정렬할 때, 각 회원 정보에 대해 lambda 함수가 반환하는 튜플을 기준으로 정렬을 수행함
# 첫 번째 요소인 x[0]을 기준으로 정렬함 (나이 순으로 정렬)
# sort()는 안정 정렬이므로, 나이가 같은 회원들은 입력된 순서대로 정렬됨
# 따라서 나이가 같은 회원들은 입력된 순서대로 정렬됨

for age, name in members:
    print(age, name)