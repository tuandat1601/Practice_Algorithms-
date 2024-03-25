import math
def solve(a, b, c):
    # Write your code here
    if  max(a,b,c)!=c and c % math.gcd(a,b)==0:
        return "YES"
    return "NO"
t = int(input().strip())

for t_itr in range(t):
    first_multiple_input = input().rstrip().split()
    a = int(first_multiple_input[0])
    b = int(first_multiple_input[1])
    c = int(first_multiple_input[2])
    result = solve(a, b, c)
    print(result)
print(math.gcd(797, 612))
