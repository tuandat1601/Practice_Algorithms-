# 345. Reverse Vowels of a String
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
def reverseVowels( s:str) :
        vowels = "aeiouAEIOU"
        vowels_str=[]
        for i in s:
            if i in vowels:
                vowels_str.append(i)
        result = ''
        for i in s:
            if i in vowels:
                i = vowels_str.pop()
            result += i
        return result
        
print(reverseVowels("aA"))
