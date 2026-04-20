add_part_list = input().split('-') # 입력된 식을 '-'로 나누어서 각 항을 리스트로 저장합니다.

# 첫번째 괄호 계산 
result = sum(map(int, add_part_list[0].split('+'))) # 첫 번째 항은 '-'로 나누기 전에 계산된 값이므로, '+'로 나누어서 계산합니다.

# 두번째 괄호를 계산해서 빼줌
for add_part in add_part_list[1:]: # 나머지 항 계산
    part_result = sum(map(int, add_part.split('+'))) # 각 항을 '+'로 나누어서 계산합니다.
    result -= part_result # 첫 번째 항에서 나머지 항들을 빼줍니다.

print(result)
