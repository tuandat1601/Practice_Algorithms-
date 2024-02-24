# Cho hai dãy số nguyên a và b, a đã sắp xếp tăng dần
# Hãy tìm mỗi phần tử của b trong a
# Trả về một xâu nhị phân nếu có phần tử thì là 1, ngược lại 0
# Dữ liệu vào:
# Dòng đầu ghi hai số nguyên dương n và m;
# Dòng thứ hai ghi n số nguyên a1, a2, ..., an;
# Dòng thứ ba ghi m số nguyên b1, b2, ..., bm.
# INPUT: 
# 7 5
# 1 2 3 4 4 6 7
# 3 1 5 4 8
# OUTPUT: 11010

n, m = map(int, input().strip().split(" "))
a= list(map(int, input().strip().split(" ")))
b= list(map(int, input().strip().split(" ")))
result = ''
def binarySearch(arr, l, r, x):
    if x > arr[len(arr)-1] or x < arr[0]:
        return '0'
    while l <= r:
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return '1'
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return '0'
for x in b:
    result+=(binarySearch(a,0,len(a)-1,x))
print(result)

# Dùng thư viện
# from bisect import bisect_left
# n, m = map(int, input().strip().split())
# a = sorted(map(int, input().strip().split()))  
# b = list(map(int, input().strip().split()))


# result = ''.join('1' if bisect_left(a, x) < n and a[bisect_left(a, x)] == x else '0' for x in b)

# print(result)