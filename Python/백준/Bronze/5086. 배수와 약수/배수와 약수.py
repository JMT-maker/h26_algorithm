import sys

def solve():
    """
    백준 5086번: 배수와 약수
    두 수가 주어졌을 때, 첫 번째 수가 두 번째 수의 약수인지, 배수인지, 아니면 둘 다 아닌지 판별합니다.
    """
    # sys.stdin.readline을 사용하여 입력 속도를 높입니다.
    input_func = sys.stdin.readline
    
    while True:
        # 두 정수 a와 b를 입력받습니다.
        a, b = map(int, input_func().split())
        
        # a와 b가 모두 0이면 입력을 종료합니다.
        if a == 0 and b == 0:
            break
            
        # 첫 번째 숫자가 두 번째 숫자의 약수인 경우
        # (두 번째 숫자를 첫 번째 숫자로 나누었을 때 나머지가 0인 경우)
        if b % a == 0:
            print("factor")
            
        # 첫 번째 숫자가 두 번째 숫자의 배수인 경우
        # (첫 번째 숫자를 두 번째 숫자로 나누었을 때 나머지가 0인 경우)
        elif a % b == 0:
            print("multiple")
            
        # 둘 다 아닌 경우
        else:
            print("neither")

if __name__ == "__main__":
    solve()