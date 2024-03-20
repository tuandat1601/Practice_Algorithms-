def modexpo(base, exponent, modulus):
    if exponent == 0:
        return 1 % modulus
    u = modexpo(base, exponent // 2, modulus)
    u = (u * u) % modulus
    if exponent % 2 == 1:
        u = (u * base) % modulus
    return u

t = int(input())
if 1 <= t <= 1000:
    arr = []
    for i in range(t):
        n = int(input().strip())
        if 0 < n < 1e12:
            result = modexpo(2, n, 10**5) - 1
            arr.append(result)
    for res in arr:
        print(res)
else:
    print("fail")

