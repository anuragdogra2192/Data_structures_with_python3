'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= first < second <= numbers.length.

Return the indices of the two numbers, index1 and index2, as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3.
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2.
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
'''
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        index1 = 0;
        index2 = len(numbers)-1;
        
        while index1 < index2:
            if numbers[index1] + numbers[index2] > target:
               index2-=1
            elif numbers[index1] + numbers[index2] < target:
                index1+=1
            else:
                return [index1+1, index2+1]

Sol = Solution();
L = [2,7,11,15]
T = 9
print(Sol.twoSum(L, T))
L1 = [2,3,4]
T1 = 6
print(Sol.twoSum(L1, T1))
L2 = [-1,0]
T2 = -1
print(Sol.twoSum(L2, T2))