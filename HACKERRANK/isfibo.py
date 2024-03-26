#  Function
#  --------
#  t = 3
#  n = 5
#  n = 7
#  n = 8
# Sample Output

# IsFibo
# IsNotFibo
# IsFibo
def isFibo(n):

    a = 0
    b = 1
    while b<n:
     
        c = a+b
        a = b
        b = c
    
    if n==b:
        return "IsFibo"
    else:
        return "IsNotFibo"