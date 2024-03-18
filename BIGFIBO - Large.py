# Dữ liệu vào: - Một dòng duy nhất chứa số nguyên không âm n.

# Dữ liệu ra: - Một dòng duy nhất chứa số nguyên là phần dư của  khi chia cho 10^9 +7.

# Input Format number
# Sample Input 0

# 10
# Sample Output 0

# 89

def modexpo(base, exponent, modulus):
    if exponent == 0:
        return 1 % modulus
    u = modexpo(base, exponent // 2, modulus)
    u = (u * u) % modulus
    if exponent % 2 == 1:
        u = (u * base) % modulus
    return u
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        fib = [1, 1]
        for i in range(2, n + 1):
            result = modexpo(fib[i - 1] + fib[i - 2], 1, 10**9+7) 
            fib.append(result)
        return fib[n]

n = int(input())
print(fibonacci(n))