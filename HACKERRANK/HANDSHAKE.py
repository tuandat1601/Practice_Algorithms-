# Có n người bạn đến dự tiệc tại nhà Cu Tí. Biết rằng mỗi người bắt tay với tất cả những người còn lại và 2 người bắt kỳ chỉ bắt tay nhau đúng 1 lần.

# Yêu cầu: Đếm số lượng cái bắt tay?
# Sample Input 0

# 2
# Sample Output 0

# 1
n = int(input())
t = n-1
print(t*(t+1)/2)