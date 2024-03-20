def matrix_power(matrix, power, modulus):
    result = [[1, 0], [0, 1]]

    while power > 0:
        if power % 2 == 1:
            result = matrix_multiply(result, matrix, modulus)
        matrix = matrix_multiply(matrix, matrix, modulus)
        power //= 2

    return result

def matrix_multiply(a, b, modulus):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
                result[i][j] %= modulus
    return result

def fibonacci_number_mod_n(n, modulus):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    

    fib_matrix = [[1, 1], [1, 0]]
    

    power_matrix = matrix_power(fib_matrix, n - 1, modulus)
    

    fib_n_mod = power_matrix[0][0] % modulus
    
    return fib_n_mod


n=int(input())


modulus = 10**9 + 7


fib_n_mod = fibonacci_number_mod_n(n+1, modulus)
print(fib_n_mod)