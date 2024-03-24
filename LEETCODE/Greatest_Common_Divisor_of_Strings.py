# 1071. Greatest Common Divisor of Strings 
# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

# Example 1:

# Input: str1 = "ABCABC", str2 = "ABC"
# Output: "ABC"
# Example 2:

# Input: str1 = "ABABAB", str2 = "ABAB"
# Output: "AB"
# Example 3:

# Input: str1 = "LEET", str2 = "CODE"
# Output: ""
 

# Constraints:

# 1 <= str1.length, str2.length <= 1000
# str1 and str2 consist of English uppercase letters.

def gcd(a:int, b:int)->int:
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
def gcdOfStrings( str1: str, str2: str) -> str:
    len1 = len(str1)
    len2 = len(str2)
    if str1+str2==str2+str1:
        
        if len1%len2==0:
            return str2
        elif len2%len1==0:
            return str2
        else:
            
            return str1[:gcd(len1,len2)]
    return  ""
print(gcdOfStrings("ABABAB","ABAB"))