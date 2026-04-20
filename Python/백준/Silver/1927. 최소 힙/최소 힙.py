import sys
input = sys.stdin.readline
#BOJ 1927
import heapq
my_heap = []

N = int(input())
for _ in range(N):
    data = int(input())
    if data == 0:
        if len(my_heap) == 0:
            print(0)
        else:
            print(heapq.heappop(my_heap))
    else: 
        heapq.heappush(my_heap, data)