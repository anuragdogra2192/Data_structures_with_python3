"""
Given a binary array nums, 
return the maximum number 
of consecutive 1's in the array.

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        count_of_zeros = 0
        global_max = 0
        
        while right < len(nums):
            
            #Expand the window
            """
            Expand our window until we meet that condition 
            but before expanding the window, process the 
            element at the ‘right’ index.
            """
            if nums[right] == 0:
                count_of_zeros +=1
                        
            #Meet the condition to stop expansion        
            #Define condition to stop expanding our window
            
            while count_of_zeros == 1:
                
            #Process the current window
                """
                If we meet our condition to stop expanding, 
                PROCESS the current window.
                """
                global_max = max(global_max, right-left)
                
                """
                Contract our current window, 
                but before contracting, 
                process the element at the ‘left’ index
                """
                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1
            right += 1
        
        if count_of_zeros < 2:
            global_max = max(global_max, right-left)
        
        return global_max