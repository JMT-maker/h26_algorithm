from collections import deque

queue = deque() #생성자, constructor

N = int(input())

# 카드를 enqueue
for i in range(N):
    queue.append(i+1)
    
while len(queue) > 1:
    print(queue.popleft(), end=' ') 
    item = queue.popleft()
    queue.append(item)

print(queue[0])