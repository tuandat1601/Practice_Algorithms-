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
    
    if base<0 and exponent%2==0:
        u= modulus-u
    return u
import math
# 10
# 199
def fibonacci(n):
    if n <= 1:
        return 1

    else:
        a,b=1,1
        for i in range(2, n + 1):
             a, b = b, (a + b) % int(1e9 + 7)
    
    return b     


n = int(input())
print(fibonacci(n))
1000000007
5000000001234