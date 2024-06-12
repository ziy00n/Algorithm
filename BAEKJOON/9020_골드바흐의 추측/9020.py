# 백준 9020_골드바흐의 추측
# 수학

T = int(input())

# 에라토스테네스의 체
# 소수판별
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


for _ in range(T):
    num = int(input())
    a = num // 2
    b = num // 2
    
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        else:
            a -= 1
            b += 1