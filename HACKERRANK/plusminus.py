# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.
# Sample Input

# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
# Sample Output

# 0.500000
# 0.333333
# 0.166667
def plusMinus(arr):
    # Write your code here
    lenarr= len(arr)
    positive=0
    negative=0
    zero=0
    for i in arr:
        if i==0:
            zero+=1
        elif i<0:
            negative+=1
        else:
            positive+=1
    print("{:.6f}".format(positive/lenarr))
    print("{:.6f}".format(negative/lenarr))
    print("{:.6f}".format(zero/lenarr))