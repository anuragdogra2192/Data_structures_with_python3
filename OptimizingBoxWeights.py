'''
Optimizing Box Weights:

An Amazon Fulfillment Associate has a set of items that need to be packed into two boxes. Given an integer array of the item weights (arr) to be packed, divide the item weights into two subsets, A and B, for packing into the associated boxes, while respecting the following conditions:

• The intersection of A and B is null.
• The union A and B is equal to the original array. The number of elements in subset A is minimal.
• The sum of A's weights is greater than the sum of B's weights.

Return the subset A in increasing order where the sum of A's weights is greater than the sum of B's weights. If more than one subset A exists, return the one with the maximal total weight.

Example:
n = 5 
arr = [3, 7, 5, 6, 2] 
The 2 subsets in arr that satisfy the conditions for A are [5, 7] and [6, 7]:
• A is minimal (size 2) 
• Sum(A) = (5 + 7) = 12 > Sum(B) = (2 + 3 + 6) = 11 
• Sum(A) = (6 + 7) = 13 > Sum() = (2 + 3 + 5) = 10 
• The intersection of A and B is null and their union is equal to arr. 
The subset A where the sum of its weight is maximal is [6, 7].
'''
def OptimizingBoxWeights(arr, n):
    arr.sort(reverse=True)
    set_B = []
    sum_A = sum(arr)
    sum_B = 0
    i = len(arr) - 1
    while((sum_A > sum_B) and i>-1):
        sum_A = sum_A - arr[i]
        sum_B += arr[i]
        if sum_B < sum_A:
            set_B.append(arr.pop())
        i -= 1
    arr.sort()
    return arr
n = 5 
arr = [3, 7, 5, 6, 2]
print(OptimizingBoxWeights(arr, n))

n = 5 
arr = [3, 70, 50, 20, 54]
print(OptimizingBoxWeights(arr, n))