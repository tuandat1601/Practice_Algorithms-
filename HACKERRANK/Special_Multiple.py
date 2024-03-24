# You are given an integer N. Can you find the least positive integer X made up of only 9's and 0's, such that, X is a multiple of N?

# Update

# X is made up of one or more occurences of 9 and zero or more occurences of 0.

# Input Format
# The first line contains an integer T which denotes the number of test cases. T lines follow.
# Each line contains the integer N for which the solution has to be found.

# Output Format
# Print the answer X to STDOUT corresponding to each test case. The output should not contain any leading zeroes.

# Constraints
# 1 <= T <= 104
# 1 <= N <= 500

# Sample Input

# 3
# 5
# 7
# 1
# Sample Output

# 90
# 9009
# 9
# Explanation
# 90 is the smallest number made up of 9's and 0's divisible by 5. Similarly, you can derive for other cases.

# Timelimits Timelimits for this challenge is given here
def solve(n):
    # Write your code here
    res =9 
    lista= [1]
    
    while res*lista[-1]%n!=0:
            lista.append(lista[-1]*10)
            for i in range(len(lista)-1):
                l = lista[-1]+lista[i]
                tr = res*l
                if tr%n==0:
                    return tr
                l= sum(lista)
                tr = res*l
                if tr%n==0:
                    return tr
    return lista[-1]*res
t = int(input().strip())

arr=[]
for t_itr in range(t):
    n = int(input().strip())
    result = solve(n)
    arr.append(result)
for x in arr:
                           


     
     print(x)
# print(sum([1,3,4]))