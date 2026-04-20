import sys

# 트리 구조를 딕셔너리로 구현
n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]

# 1. 전위 순회 (Root -> L -> R)
def pre_order(node):
    if node == '.':
        return
    print(node, end='')      # 루트 출력
    pre_order(tree[node][0]) # 왼쪽 탐색
    pre_order(tree[node][1]) # 오른쪽 탐색

# 2. 중위 순회 (L -> Root -> R)
def in_order(node):
    if node == '.':
        return
    in_order(tree[node][0])  # 왼쪽 탐색
    print(node, end='')      # 루트 출력
    in_order(tree[node][1])  # 오른쪽 탐색

# 3. 후위 순회 (L -> R -> Root)
def post_order(node):
    if node == '.':
        return
    post_order(tree[node][0]) # 왼쪽 탐색
    post_order(tree[node][1]) # 오른쪽 탐색
    print(node, end='')       # 루트 출력

# 결과 출력
pre_order('A')
print()
in_order('A')
print()
post_order('A')