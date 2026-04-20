N = int(input())
paper = []
color_list = []

for _ in range(N):
    paper.append(list(map(int, input().split())))

def makePaper(row, col, size): # row, col: 현재 영역의 시작 위치, size: 현재 영역의 크기
    # 현재 영역이 모두 같은 색인지 확인
    color = paper[row][col] # 현재 영역의 색상 (0 또는 1)
    for i in range(row,row+size):# row부터 row+size까지 반복
        for j in range(col,col+size):# col부터 col+size까지 반복
            if paper[i][j] != color:   # 현재 색과 다른 색이 발견되면
                # 같은 색이 아니면, 영역을 나누어정복 
                new_size = size // 2 # 새로운 영역의 크기 (현재 크기의 절반)
                # row, col, new_size
                makePaper(row, col, new_size) # 1사분면 (왼쪽 위)
                makePaper(row, col + new_size, new_size) # 2사분면 (오른쪽 위)
                makePaper(row + new_size, col, new_size) # 3사분면 (왼쪽 아래)
                makePaper(row + new_size, col + new_size, new_size) # 4사분면 (오른쪽 아래)
                return # 재귀 호출 후 반환 (현재 영역은 더 이상 처리할 필요 없음)
    # 모두 같은 색일 때, 현재 색을 color_list에 추가
    color_list.append(color)

makePaper(0,0,N)
print(color_list.count(0))
print(color_list.count(1))
