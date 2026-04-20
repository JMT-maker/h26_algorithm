import sys

# 재귀 깊이 제한 해제 (기본값이 낮아 런타임 에러가 날 수 있음)
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
count = 0

# 모든 정점을 순회하며 방문하지 않은 정점이 있다면 탐색 시작
for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1 # 한 번의 탐색이 끝나면 연결 요소 1개 발견!

print(count)