import sys

# 1. 단어 개수 입력
n = int(sys.stdin.readline())

# 2. 단어 입력받기 (중복 제거를 위해 set 사용)
word_set = set()
for _ in range(n):
    word_set.add(sys.stdin.readline().strip()) # 입력받은 단어에서 양쪽 공백 제거 후 set에 추가 (중복 제거)

# 3. 리스트로 변환 (정렬을 하기 위함)
word_list = list(word_set) # set은 순서가 없기 때문에, 정렬을 위해 리스트로 변환함

# 4. 정렬 기준 설정
# 첫 번째 기준: len(x) (길이 순)
# 두 번째 기준: x (사전 순)
word_list.sort(key=lambda x: (len(x), x))# sort() 메서드에 key 매개변수로 lambda 함수를 전달하여 정렬 기준을 설정함
# lambda 함수는 각 단어 x에 대해 (len(x), x) 튜플을 반환함
# sort() 메서드는 리스트를 정렬할 때, 각 단어에 대해 lambda 함수가 반환하는 튜플을 기준으로 정렬을 수행함
# 첫 번째 요소인 len(x)를 기준으로 정렬하고, len(x)가 같은 경우에는 두 번째 요소인 x를 기준으로 정렬함
# 따라서 단어의 길이가 짧은 순서대로 정렬되고, 길이가 같은 단어들끼리는 사전 순으로 정렬됨
# 정렬된 word_list를 순회하면서 각 단어를 출력함
# print(*word_list, sep='\n')와 같이 unpacking을 사용하여 간단하게 출력할 수도 있음
# print(*word_list, sep='\n') # word_list의 요소를 언팩하여 각 단어를 줄바꿈으로 구분하여 출력
# 위의 print(*word_list, sep='\n')는 word_list의 요소를 언팩하여 각 단어를 줄바꿈으로 구분하여 출력하는 방식으로, word_list의 각 단어를 개별적으로 출력하는 것과 동일한 결과를 얻을 수 있음
# 하지만 명시적으로 각 단어를 출력하는 방식이 더 명확할 수 있음
# 따라서 for 루프를 사용하여 각 단어를 출력하는 방식을 선택함


# 5. 결과 출력
for word in word_list:
    print(word)