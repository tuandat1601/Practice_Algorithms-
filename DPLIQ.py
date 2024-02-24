# Dãy con tăng dài nhất
# Hãy cho biết dãy con đơn điệu tăng của dãy đã cho có nhiều nhất bao nhiêu số hạng?
# Dữ liệu vào:
# Dòng đầu chứa số nguyên dương N;
# Dòng thứ hai chứa N số nguyên dương , mỗi số cách nhau bởi một dấu cách.
# Dữ liệu ra:
# Ghi ra độ dài của dãy con đơn điệu tăng dài nhất.
# INPUT:
#  6
# 1 2 5 4 6 2
# OUTPUT:
# 4
# Dãy con đó là 1, 2, 4, 6 hoặc 1 2 5 6

n= int(input())
nums= list(map(int, input().strip().split(" ")))
dp = [0] * n
dp[0]=1
for i in range(1,n):
    x=0
    for j in range(i):
        if (nums[j]<nums[i]):
            if dp[j]>x:
                x = dp[j]
    dp[i] = x + 1
print(max(dp))

            
