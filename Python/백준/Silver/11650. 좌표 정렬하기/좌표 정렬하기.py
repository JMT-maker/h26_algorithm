import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))

points.sort()

for point in points:
    print(point[0], point[1])