import sys

def get_gcd(a, b):
    """
    유클리드 호제법을 사용하여 최대공약수(GCD)를 구하는 함수
    """
    while b != 0:
        a, b = b, a % b
    return a

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    t = int(input_data[0])
    results = []

    idx = 1
    for _ in range(t):
        a = int(input_data[idx])
        b = int(input_data[idx + 1])
        idx += 2

        gcd = get_gcd(a, b)

        lcm = (a * b) // gcd
        results.append(str(lcm))

    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()