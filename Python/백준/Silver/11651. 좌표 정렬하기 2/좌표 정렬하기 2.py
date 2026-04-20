#2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, 
#y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 
#다음 출력하는 프로그램을 작성하시오.

#첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 
#둘째 줄부터 N개의 줄에는 i번점의 위치 x_i와 y_i가 주어진다. 
#(-100,000 ≤ x_i, y_i ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

import sys
input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    x,y = map(int, input().split()) # x좌표와 y좌표를 입력받아서, points 리스트에 [y, x] 형태로 저장함
    points.append([y, x])# y좌표가 증가하는 순으로 정렬하기 위해, 각 점을 [y, x] 형태로 저장함
# points 리스트는 각 점을 [y, x] 형태로 저장하므로, sort() 메서드를 사용하여 points 리스트를 정렬하면, y좌표가 증가하는 순으로 정렬되고, y좌표가 같은 경우에는 x좌표가 증가하는 순으로 정렬됨       


points.sort()

for p in points: # 정렬된 points 리스트를 순회하면서 각 점의 y좌표와 x좌표를 출력함
    # print(*p) # p 리스트의 요소를 언팩하여 출력
    print(p[1], p[0]) # p 리스트는 [y, x] 형태로 저장되어 있으므로, 출력할 때는 x좌표(p[1])와 y좌표(p[0])를 각각 출력함
    # 정렬된 points 리스트를 순회하면서 각 점의 y좌표와 x좌표를 출력함
    # print(*p)와 같이 unpacking을 사용가능





    