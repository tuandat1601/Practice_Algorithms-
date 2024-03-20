def power_mod(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus
    return result

# modulus = int(1e5)
# exponent = 100000000000
# result = power_mod(2, exponent, modulus)
# print(result)
   
#function that calculate modular exponentiation x^n mod m.
def modpower(x, n, m):
    print(x, n, m)
    if n == 0: # base case
        return 1 % m
    u = modpower(x, n // 2, m)
    print("first u ",u)
    u = (u * u) % m
    print("seccond u ",u)
    if n % 2 == 1: # when 'n' is odd
        u = (u * x) % m
        print("third u ",u)
    return u
 
#driver function
print(625//7)
print(modpower(5, 8, 7))