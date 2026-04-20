N = int(input())

# 자료 구조 정의 
# [Comparison] 5kg 봉지의 최대 개수부터 0개까지 모든 경우의 수 확인
max_5kg_bags = N // 5
max_3kg_bags = N // 3
min_bags = max_5kg_bags + max_3kg_bags  # 충분히 큰 값으로 초기화
is_found = False # 조합을 찾았는지 여부를 나타내는 플래그 변수  

# 알고리즘 
for num_5kg in range(max_5kg_bags + 1): # 5kg 봉지의 개수는 0개부터 최대 개수까지
    for num_3kg in range(max_3kg_bags + 1): # 3kg 봉지의 개수는 0개부터 최대 개수까지
        if (5 * num_5kg) + (3 * num_3kg) == N: # 현재 조합이 목표 무게와 일치하는지 확인
            is_found = True # 조합을 찾았음을 표시
            cur_bags = num_5kg + num_3kg # 현재 조합의 봉지 수 계산
            if min_bags > cur_bags: # 현재 조합이 최소 봉지 수보다 작은지 확인
                min_bags = cur_bags # 최소 봉지 수 업데이트
            # min_bags = min(min_bags, num_5kg + num_3kg) # 최소 봉지 수 업데이트
if is_found:
    print(min_bags) # 최소 봉지 수 출력
else:
    print(-1) # 조합을 찾지 못한 경우   