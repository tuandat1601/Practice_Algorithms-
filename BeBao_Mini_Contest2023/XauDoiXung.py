# Cho xâu S, hãy cho biết cần thay đổi ít nhất bao nhiêu kí tự để
# S tồn tại xâu con có độ dài lớn hơn  là xâu đối xứng.
# INPUT:
# 2
# dcbefab
# xyzyx
# OUTPUT:
# 1
# 0
def checkPalindrome(s: str):
    lengstr = len(s)
    if lengstr>1:
        s+="#"
        for i in range(0,lengstr-1):
            if lengstr == 2:
                if s[i] ==s[i+1] :
                    return 0
            elif s[i] ==s[i+1] or s[i] ==s[i+2]:
                return 0
        return 1
    return -1


n = int(input())
arr = list()
for i in range(n):
    arr.append(str(input().strip()))
for s in arr:
    print(checkPalindrome(s))
