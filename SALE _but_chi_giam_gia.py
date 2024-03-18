# Cu Tí được phân công mua bút chì cho cả lớp nhân dịp đầu năm học mới. Số bút chì cần mua là n. 
# Trong cửa hàng, giá mua lẻ mỗi chiếc bút chì là p. Tuy nhiên cu Tí là học sinh nên được cửa hàng cho hưởng chính sách ưu đãi đầu năm học mới.
# Cụ thể là cứ mỗi k chiếc bút chì mà cu Tí mua thì cậu ta sẽ được cửa hàng tặng thêm cho 1 chiếc bút chì nữa.

# Yêu cầu: Xác định số tiền tối thiểu mà cu Tí cần mang theo để có thể tới cửa hàng mang về ít nhất n chiếc bút chì.
# Sample Input 0

# 984 39 429
# Sample Output 0

# 411840
n, k, p = map(int, input().split())
km = p * k
tien = (n // (k + 1)) * km
if n % (k + 1) != 0:
    tien += (n % (k + 1)) * p
print(tien)

