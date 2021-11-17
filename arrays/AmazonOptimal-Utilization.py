'''
Given 2 lists a and b. Each element is a pair of integers 
where the first integer represents the unique id and the second integer represents a value. 
Your task is to find an element from a and an element form b such that the sum of their values is less 
or equal to target and as close to target as possible. Return a list of ids of selected elements. 
If no pair is possible, return an empty list.

Input:
a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

Output: [[2, 1]]

Explanation:
There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

Input:
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

Output: [[1, 3], [3, 2]]
'''
def Optimal_Utilization(a, b, target):
    nearest_value = 0
    i = len(a) - 1
    j = len(b) - 1 
    Output = []
    while i >= 0 and j >= 0:
        temp = a[i][1] + b[j][1]
        if(temp > target):
            i -= 1
        elif(temp <= target):
            if(nearest_value == temp):
                Output.append([a[i][0], b[j][0]])
            elif(nearest_value < temp):
                nearest_value = temp
                Output = [[a[i][0], b[j][0]]]
            j -= 1
            i = len(a) - 1
    
    return Output
                
a = [[1, 8], [2, 15], [3, 9]]
b = [[1, 8], [2, 11], [3, 12]]
target = 20

print(Optimal_Utilization(a, b, target))

a = [[1, 2], [2, 4], [3, 6]]
b = [[1, 2]]
target = 7

print(Optimal_Utilization(a, b, target))

a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10
print(Optimal_Utilization(a, b, target))
